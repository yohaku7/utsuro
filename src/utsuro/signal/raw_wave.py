"""ファイルなどから読み込んだ生のデータ。"""
import numpy as np

from .wave import Wave


class RawWave(Wave):
    def __init__(self, data: np.ndarray, fs: int):
        assert fs > 0

        self.data = data
        self._fs = fs
        self._duration: float = np.divide(len(data), fs)

    def generate(self) -> np.ndarray:
        return self.data

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def fs(self) -> int:
        return self._fs
