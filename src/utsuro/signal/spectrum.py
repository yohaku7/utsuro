"""スペクトラムの計算。"""
from typing import Literal

import matplotlib.pyplot as plt
import numpy as np

from utsuro.plot import PlotParam
from .wave import Wave

type SpectrumType = Literal["amplitude"] | Literal["power"] | Literal["log"] | Literal["log_power"]


_PLOT_TITLE_YLABEL = {
    "amplitude": ("Amplitude Spectrum", "Amplitude"),
    "power": ("Power Spectrum", "Power"),
    "log": ("Log Spectrum", "Log Amplitude [dB]"),
    "log_power": ("Log Power Spectrum", "Log Power [dB]"),
}
_PLOT_PARAM = {
    k: PlotParam(v[0], "Frequency [Hz]", v[1]) for k, v in _PLOT_TITLE_YLABEL.items()
}


class Spectrum:
    def __init__(self, wave: Wave, type: SpectrumType):
        self.wave = wave
        self.type = type

    def get(self) -> tuple[np.ndarray, np.ndarray]:
        data = self.wave.generate()

        fft = np.fft.rfft(data)
        fftfreq = np.fft.rfftfreq(len(data), np.divide(1.0, self.wave.fs))

        match self.type:
            case "amplitude":
                fft = np.abs(fft)
            case "power":
                fft = np.pow(np.abs(fft), 2)
            case "log":
                fft = np.log10(np.abs(fft) + 1e-9)
            case "log_power":
                fft = 10 * np.log10(np.pow(np.abs(fft), 2) + 1e-9)

        return fftfreq, fft

    def _get_param(self) -> PlotParam:
        return _PLOT_PARAM[self.type]

    def plot(self) -> None:
        freq, fft = self.get()

        plt.figure(figsize=(10, 6))
        plt.xlim(0, 4000)
        plt.title(_PLOT_PARAM[self.type].title)
        plt.xlabel(_PLOT_PARAM[self.type].x_label)
        plt.ylabel(_PLOT_PARAM[self.type].y_label)
        plt.tight_layout()
        plt.plot(freq, fft)
        plt.show()
