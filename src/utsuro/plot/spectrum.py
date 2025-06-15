"""スペクトラムの表示。"""
import matplotlib.pyplot as plt
import numpy as np

from utsuro.signal import Wave


def plot(wave: Wave) -> None:
    data = wave.generate()

    fft = np.fft.rfft(data)
    freq = np.fft.rfftfreq(len(data), np.divide(1.0, wave.fs))

    # 絶対値をとる
    fft = np.abs(fft)

    plt.figure(figsize=(10, 6))
    plt.xlim(0, 4000)
    plt.title("Spectrum")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.plot(freq, fft)
    plt.show()
