import sounddevice as sd
import numpy as np
from typing import Callable
from models.pitch import Pitch


class Stream(sd.InputStream):
    def device_to_stream_callback(self, in_data: np.ndarray, out_data: np.ndarray, frames, time, status):
        pass

    def __init__(self, stream_to_view_callback: Callable[[Pitch, float], None]):
        super().__init__(callback=self.device_to_stream_callback)
