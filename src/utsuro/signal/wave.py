"""すべての波を表す基底クラス。"""
from abc import ABC, abstractmethod

import numpy as np


class Wave(ABC):
    @abstractmethod
    def generate(self) -> np.ndarray:
        pass
