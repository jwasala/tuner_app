from dataclasses import dataclass
from typing import Callable, List, Tuple
import sounddevice as sd
import numpy as np
from models.constants import BLOCK_SIZE, SAMPLING_RATE, SECONDS_TO_TUNE, BACKLOG_SIZE
from models.pitch import Pitch
from models.sample import Sample
from models.tunings import TUNINGS


@dataclass
class TuningStatus:
    closest_pitch: Pitch
    freq: float
    freq_diff: float
    freq_diff_normalized: float
    strings: List[Tuple[Pitch, float]]


class Stream(sd.InputStream):

    def read_input(self, indata: np.ndarray, frames, time, status) -> None:
        if len(self.backlog) >= BACKLOG_SIZE * BLOCK_SIZE:
            self.backlog = self.backlog[BLOCK_SIZE:]

        self.backlog = np.append(self.backlog, indata)

        sample = Sample(self.backlog)
        print(sample.power)
        freq = sample.harmonic_product_spectrum()

        pitch = Pitch.from_frequency(freq)

        # update progress of tuning string if pitch matches with the string
        if pitch.is_within_error_margin(freq):
            for i in range(len(self.strings_status)):
                if self.strings_status[i][0] == pitch:
                    self.strings_status[i] = (
                        pitch, min(1, self.strings_status[i][1] + (BLOCK_SIZE / (SAMPLING_RATE * SECONDS_TO_TUNE))))

        self.update_view(TuningStatus(pitch, freq, freq - pitch.frequency,
                                      (freq - pitch.frequency) * 2 / (pitch.frequency - pitch.shift(-1).frequency),
                                      self.strings_status))

    def __init__(self, update_view: Callable[[TuningStatus], None]):
        super().__init__(
            callback=lambda indata, frames, time, status: self.read_input(indata, frames, time, status),
            channels=1,
            samplerate=SAMPLING_RATE,
            blocksize=BLOCK_SIZE
        )
        self.update_view = update_view
        self.strings_status = [(string, 0) for string in TUNINGS['guitar']['standard']]
        self.backlog = np.array([])
