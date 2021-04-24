import numpy as np
from models.pitch import Pitch


class Sample:
    def __init__(self, data: np.ndarray):
        self.data = data

    def estimate_frequency(self) -> float:
        pass

    def closest_pitch(self) -> Pitch:
        pass
