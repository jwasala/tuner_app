import numpy as np


class Sample:
    def __init__(self, rate: int, data: np.ndarray):
        self.rate = rate
        self.data = data

    @property
    def duration(self):
        return len(self.data) / self.rate

    @property
    def power(self):
        """
        :return: Signal power of the sample.
        """
        return np.sum([x ** 2 for x in self.data]) / len(self.data)

    def estimate_frequency(self) -> float:
        """
        Estimates frequency of the sample using Harmonic Product Spectrum.

        :return: Estimated frequency.
        """
