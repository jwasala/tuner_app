import numpy as np
import scipy.fftpack
from models.constants import SAMPLING_RATE


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

    def simple_discrete_fourier_transform(self) -> np.ndarray:
        """
        Transforms sample data from displacement domain to frequency domain without noise reduction.
        """
        window = np.hanning(len(self.data))
        flat_data = self.data.flatten()
        dft = abs(scipy.fftpack.fft(flat_data * window))

        return dft[:len(dft) // 2]

    def noise_reduced_discrete_fourier_transform(self) -> np.ndarray:
        """
        Transforms sample data from displacement domain to frequency domain.
        After that, various noise reduction techniques are applied in order to enhance signal.
        """
        pass

    def harmonic_product_spectrum(self) -> float:
        """
        Estimates frequency of the sample using Harmonic Product Spectrum.

        :return: Estimated frequency.
        """
        pass
