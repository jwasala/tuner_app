from typing import Callable
import sounddevice as sd
import numpy as np
from models.constants import BLOCK_SIZE, SAMPLING_RATE
from models.pitch import Pitch
from models.sample import Sample


class Stream(sd.InputStream):
    def input_to_model(self, indata: np.ndarray, frames, time, status) -> None:
        sample = Sample(indata)
        freq = np.argmax(sample.discrete_fourier_transform())

        if type(freq) == np.ndarray:
            freq = freq[0]

        pitch = Pitch.from_frequency(freq)

        self.model_to_view(pitch, freq)

    def __init__(self, model_to_view: Callable[[Pitch, float], None]):
        super().__init__(
            callback=lambda indata, frames, time, status: self.input_to_model(indata, frames, time, status),
            channels=1,
            samplerate=SAMPLING_RATE,
            blocksize=BLOCK_SIZE
        )
        self.model_to_view = model_to_view