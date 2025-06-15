"""sm13283644 の周波数・振幅のデータ。"""
# refer: https://www.nicovideo.jp/watch/sm13283644
from typing import Final, Literal

from utsuro.signal import CompositeWave

DEFAULT_F0: Final[Literal[260]] = 260


def vowel_A(*, f0: int = DEFAULT_F0, duration: float, fs: int = 48000) -> CompositeWave:
    return CompositeWave(
        [
            (f0    , 0.07),
            (f0 * 2, 0.09),
            (f0 * 3, 0.08),
            (f0 * 4, 0.19),
            (f0 * 5, 0.08),
            (f0 * 6, 0.07),
        ],
        duration=duration,
        fs=fs,
    )


def vowel_I(*, f0: int = DEFAULT_F0, duration: float, fs: int = 48000) -> CompositeWave:
    return CompositeWave(
        [
            (f0     , 0.52),
            (f0 *  2, 0.03),
            (f0 * 11, 0.02),
            (f0 * 12, 0.01),
            (f0 * 13, 0.02),
        ],
        duration=duration,
        fs=fs,
    )


def vowel_U(*, f0: int = DEFAULT_F0, duration: float, fs: int = 48000) -> CompositeWave:
    return CompositeWave(
        [
            (f0    , 0.32),
            (f0 * 2, 0.11),
            (f0 * 4, 0.02),
            (f0 * 5, 0.02),
            (f0 * 6, 0.13),
        ],
        duration=duration,
        fs=fs,
    )


def vowel_E(*, f0: int = DEFAULT_F0, duration: float, fs: int = 48000) -> CompositeWave:
    return CompositeWave(
        [
            (f0     , 0.18),
            (f0 *  2, 0.14),
            (f0 *  3, 0.13),
            (f0 *  4, 0.03),
            (f0 * 11, 0.03),
        ],
        duration=duration,
        fs=fs,
    )


def vowel_O(*, f0: int = DEFAULT_F0, duration: float, fs: int = 48000) -> CompositeWave:
    return CompositeWave(
        [
            (f0    , 0.11),
            (f0 * 2, 0.14),
            (f0 * 3, 0.10),
            (f0 * 4, 0.24),
        ],
        duration=duration,
        fs=fs,
    )
