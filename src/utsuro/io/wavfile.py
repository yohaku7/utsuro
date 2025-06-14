"""WAV ファイルの読み込みと書き出し。"""
from enum import Enum, auto
from logging import getLogger

import numpy as np
import scipy.io.wavfile as wav

logger = getLogger(__name__)


class WavFileFormat(Enum):
    """WAV ファイルのフォーマット"""

    # floating-point
    FLOAT_32bit = auto()

    # PCM
    PCM_16bit = auto()
    PCM_24bit = auto()
    PCM_32bit = auto()


# TODO: wavファイルのフォーマットを変更できるようにする
def read(path: str, *, format: WavFileFormat | None = None) -> np.ndarray:
    fs, data = wav.read(path)

    logger.info(f"Read WAV file at: {path}")

    return data


# TODO: wavファイルのフォーマットを変更できるようにする
def write(path: str, wave, *, format: WavFileFormat | None = None) -> None:
    wav.write(path, wave.fs, wave.generate())

    logger.info(f"WAV file wrote at: {path}")
