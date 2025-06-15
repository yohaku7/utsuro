"""すべての波を表す基底クラス。"""
from abc import ABC, abstractmethod

import numpy as np


class Wave(ABC):
    @abstractmethod
    def generate(self) -> np.ndarray:
        pass

    @property
    @abstractmethod
    def duration(self) -> float:
        pass

    @property
    @abstractmethod
    def fs(self) -> int:
        pass

    def generate_time_axis(self) -> np.ndarray:
        return np.linspace(
            0, self.duration, int(self.fs * self.duration), endpoint=False,
        )
