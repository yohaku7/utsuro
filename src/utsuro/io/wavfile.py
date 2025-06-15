"""WAV ファイルの読み込みと書き出し。"""
from enum import Enum, auto
from logging import getLogger

import scipy.io.wavfile as wav

from utsuro.signal import RawWave, Wave

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
def read(path: str, *, format: WavFileFormat | None = None) -> RawWave:
    fs, data = wav.read(path)

    logger.info("Read WAV file at: %s", path)

    return RawWave(data, fs)


# TODO: wavファイルのフォーマットを変更できるようにする
def write(path: str, wave: Wave, *, format: WavFileFormat | None = None) -> None:
    wav.write(path, wave.fs, wave.generate())

    logger.info("WAV file wrote at: %s", path)
