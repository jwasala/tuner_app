from typing import Callable
import sounddevice as sd
import numpy as np
from models.pitch import Pitch


class Stream(sd.InputStream):
    def input_to_model(self, indata: np.ndarray, frames, time, status) -> None:
        pass

    def __init__(self, model_to_view: Callable[[Pitch, float], None]):
        super().__init__(
            callback=lambda indata, frames, time, status: self.input_to_model(indata, frames, time, status),
            channels=1
        )
        self.model_to_view = model_to_view
