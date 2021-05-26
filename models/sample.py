import copy

import numpy as np
import scipy.fftpack
from models.constants import SAMPLING_RATE, LOW_FREQUENCY, MAX_DOWNSAMPLING


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
        flat_data = self.data.flatten()
        dft = abs(scipy.fftpack.fft(flat_data * window))

        for i in range(LOW_FREQUENCY):
            dft[i] = 0

        return dft[:len(dft) // 2, HIGH_FREQUENCY]

    def harmonic_product_spectrum(self, simple=True) -> float:
        """
        Estimates frequency of the sample using Harmonic Product Spectrum.

        :return: Estimated frequency.
        """
        if simple:
            freq = np.argmax(self.discrete_fourier_transform())
        else:
            window = np.hanning(len(self.data))
            flat_data = self.data.flatten()
            dft = abs(scipy.fftpack.fft(flat_data * window))

            # ignore hum
            for i in range(LOW_FREQUENCY):
                dft[i] = 0
            dft = dft[:len(dft) // 2]

            dft_copy = copy.deepcopy(dft)

            for i in range(MAX_DOWNSAMPLING):
                dft_copy = np.multiply(dft_copy[:int(np.ceil(len(dft_copy) / (i + 1)))], dft_copy[::(i + 1)])

            freq = np.argmax(dft)

        return freq * (SAMPLING_RATE / len(self.data))
