"""窓の計算。"""
from typing import Literal

import numpy as np

type WindowType = Literal["hanning"] | Literal["hamming"]


def apply_window(data: np.ndarray, type: WindowType, *, correction: bool = False) -> np.ndarray:
    N = len(data)
    match type:
        case "hanning":
            w = np.hanning(N)
        case "hamming":
            w = np.hamming(N)
        case _:
            raise ValueError("Illegal window type")

    if correction:
        w = w / np.sum(w)

    return data * w
