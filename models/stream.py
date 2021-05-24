from dataclasses import dataclass
from typing import Callable, List, Tuple
import sounddevice as sd
import numpy as np
from models.constants import BLOCK_SIZE, SAMPLING_RATE, SECONDS_TO_TUNE, BACKLOG_SIZE, SUPPRESSION_FACTOR
from models.pitch import Pitch, Note
from models.sample import Sample
from models.tunings import TUNINGS


@dataclass
class TuningStatus:
    closest_pitch: Pitch
    freq: float
    freq_diff: float
    freq_diff_regularized: float
    sample_power: float
    strings: List[Tuple[Pitch, float]]


class Stream(sd.InputStream):

    def change_strings(self, new_strings):
        self.strings_status = new_strings

    def read_input(self, indata: np.ndarray, frames, time, status) -> None:
        if len(self.indata_backlog) >= BACKLOG_SIZE * BLOCK_SIZE:
            self.indata_backlog = self.indata_backlog[BLOCK_SIZE:]

        self.indata_backlog *= SUPPRESSION_FACTOR
        self.indata_backlog = np.append(self.indata_backlog, indata.flatten())
        sample = Sample(self.indata_backlog)
        freq = sample.estimate_frequency()

        pitch = Pitch.from_frequency(freq)

        # update progress of tuning string if pitch matches with the string
        if pitch.is_within_error_margin(freq):
            for i in range(len(self.strings_status)):
                if self.strings_status[i][0] == pitch:
                    self.strings_status[i] = (
                        pitch, min(1, self.strings_status[i][1] + (BLOCK_SIZE / (SAMPLING_RATE * SECONDS_TO_TUNE))))

        self.status = TuningStatus(
            closest_pitch=pitch,
            freq=freq,
            freq_diff=freq - pitch.frequency,
            freq_diff_regularized=(freq - pitch.frequency) / abs(pitch.frequency - pitch.shift(-1).frequency),
            sample_power=sample.power,
            strings=self.strings_status
        )

    def __init__(self):
        super().__init__(
            callback=lambda indata, frames, time, status: self.read_input(indata, frames, time, status),
            channels=1,
            samplerate=SAMPLING_RATE,
            blocksize=BLOCK_SIZE
        )
        self.strings_status = [(string, 0) for string in TUNINGS['guitar standard']]
        self.status = TuningStatus(Pitch(Note.A, 4), 440, 0, 0, 1.0e-3, self.strings_status)
        self.indata_backlog = np.array([])
