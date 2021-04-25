import numpy as np


class Sample:
    def __init__(self, data: np.ndarray):
        self.data = data

    def estimate_frequency(self) -> float:
        pass
