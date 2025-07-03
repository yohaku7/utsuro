"""ケプストラムの計算。"""
import matplotlib.pyplot as plt
import numpy as np

from .wave import Wave
from .window import apply_window


class Cepstrum:
    def __init__(self, wave: Wave, *, start: int = 100, count: int = 2 ** 14):
        assert start >= 0
        assert count > 0

        self.wave = wave
        self.start = start
        self.count = count

        self.To_low = self.wave.fs // 800
        self.To_high = self.wave.fs // 40

    def get_frequency_axis(self) -> np.ndarray:
        return np.fft.rfftfreq(self.count, np.divide(1.0, self.wave.fs))

    def get_quefrency_axis(self) -> np.ndarray:
        return np.arange(self.count) * 1000 / self.wave.fs

    def get_cepstrum(self) -> np.ndarray:
        data = self.wave.generate()

        # 範囲指定
        data = data[self.start : self.start + self.count]

        # 窓
        data = apply_window(data, "hanning", correction=True)

        fft = np.fft.rfft(data)

        # 対数変換
        fft = np.abs(fft)
        fft = np.log10(fft + 1e-9)

        ceps = np.fft.irfft(fft)
        return ceps

    def _get_lifter_threshold(self) -> np.signedinteger:
        # 基本周期を推定し、その半分までをリフタリングの閾値とする
        ceps = self.get_cepstrum()

        To = np.argmax(ceps[self.To_low:self.To_high]) + self.To_low
        lifter = To // 2

        return lifter

    def get_spectrum_envelope(self) -> np.ndarray:
        ceps = self.get_cepstrum()

        # リフタリング
        lifter = self._get_lifter_threshold()
        ceps[:lifter] = 0
        ceps[self.count - lifter + 1 :] = 0

        envelope = np.real(np.fft.rfft(ceps))
        return envelope

    def get_spectral_fine_component(self) -> np.ndarray:
        ceps = self.get_cepstrum()

        # リフタリング
        lifter = self._get_lifter_threshold()
        ceps[lifter : self.count - lifter + 1] = 0

        fine = np.real(np.fft.rfft(ceps))
        return fine

    def plot_cepstrum(self) -> None:
        t = self.get_quefrency_axis()
        ceps = self.get_cepstrum()

        # ylim = np.max(ceps[self.To_low:self.To_high])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(0, 30)
        ax.set_ylim(-0.1, 0.1)
        ax.set_xlabel("Quefrency [ms]")
        ax.set_ylabel("Log Amplitude")
        ax.plot(t, ceps)

        plt.show()
