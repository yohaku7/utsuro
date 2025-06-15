"""波形の描画。"""
import matplotlib.pyplot as plt

from utsuro.signal import Wave


def plot(wave: Wave) -> None:
    data = wave.generate()
    t = wave.generate_time_axis()

    plt.figure(figsize=(10, 6))
    plt.xlim(0, 0.02)
    plt.title("Waveform")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")  # FIXME: ラベルの名前をどうするか？
    plt.tight_layout()
    plt.plot(t, data)
    plt.show()
