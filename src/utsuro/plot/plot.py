"""プロット用のデータを格納するクラス。"""
import numpy as np
import matplotlib.pyplot as plt


class Plot:
    @staticmethod
    def plot(t: np.ndarray, y: np.ndarray,
             *, xlim: tuple[float, float], ylim: tuple[float, float],
             xlabel: str, ylabel: str) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.plot(t, y)

        plt.show()
