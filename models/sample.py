import numpy as np
import scipy.fftpack
from models.constants import SAMPLING_RATE, LOW_FREQUENCY, HIGH_FREQUENCY, MAX_DOWNSAMPLING


class Sample:
    def __init__(self, data: np.ndarray):
        self.data = data

    @property
    def duration(self) -> float:
        return len(self.data) / SAMPLING_RATE

    @property
    def power(self) -> float:
        """
        :return: Signal power of the sample.
        """
        return np.sum([x ** 2 for x in self.data]) / len(self.data)

    def discrete_fourier_transform(self) -> np.ndarray:
        """
        Transforms sample data from displacement domain to frequency domain.
        """
        window = np.hanning(len(self.data))
        dft = abs(scipy.fftpack.fft(self.data * window))

        # ignore hum
        for i in range(LOW_FREQUENCY):
            dft[i] = 0

        return dft[:min(len(dft) // 2, HIGH_FREQUENCY)]

    def estimate_frequency(self) -> float:
        """
        Estimates frequency for a given sample.
        """
        dft = self.discrete_fourier_transform()

        freq = np.argmax(dft)

        if type(freq) == np.ndarray:
            freq = freq[0]

        return freq * (SAMPLING_RATE / len(self.data))
