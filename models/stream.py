from dataclasses import dataclass
from typing import Callable, List, Tuple
import sounddevice as sd
import numpy as np
from models.constants import BLOCK_SIZE, SAMPLING_RATE
from models.pitch import Pitch, Note
from models.sample import Sample

TUNINGS = {
    'guitar': {
        'standard': [
            Pitch(Note.E, 2),
            Pitch(Note.A, 2),
            Pitch(Note.D, 3),
            Pitch(Note.G, 3),
            Pitch(Note.B, 3),
            Pitch(Note.E, 4)
        ],
        'half-step down': [
            Pitch(Note.DSharp, 2),
            Pitch(Note.GSharp, 2),
            Pitch(Note.CSharp, 3),
            Pitch(Note.FSharp, 3),
            Pitch(Note.ASharp, 3),
            Pitch(Note.DSharp, 4)
        ]
    }
}


@dataclass
class TuningStatus:
    closest_pitch: Pitch
    freq: float
    strings: List[Tuple[Pitch, bool]]


class Stream(sd.InputStream):

    def read_input(self, indata: np.ndarray, frames, time, status) -> None:
        sample = Sample(indata)
        freq = np.argmax(sample.discrete_fourier_transform())

        if type(freq) == np.ndarray:
            freq = freq[0]

        pitch = Pitch.from_frequency(freq)

        self.update_view(TuningStatus(pitch, freq, self.strings_status))

    def __init__(self, update_view: Callable[[TuningStatus], None]):
        super().__init__(
            callback=lambda indata, frames, time, status: self.read_input(indata, frames, time, status),
            channels=1,
            samplerate=SAMPLING_RATE,
            blocksize=BLOCK_SIZE
        )
        self.update_view = update_view
        self.strings_status = [(string, False) for string in TUNINGS['guitar']['standard']]
