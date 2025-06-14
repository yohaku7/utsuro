"""sin 波の生成。"""
from dataclasses import dataclass

import numpy as np

from .wave import Wave


# type alias
type SineWaveParamType = SineWaveParam | tuple[int, float] | tuple[int, float, float]


@dataclass(frozen=True)
class SineWaveParam:
    frequency: int
    amplitude: float
    phase: float = 0.0

    def __post_init__(self):
        assert self.frequency > 0
        assert self.amplitude >= 0


# helper
def _convert_param(val: SineWaveParamType) -> SineWaveParam:
    if isinstance(val, SineWaveParam):
        return val
    elif isinstance(val, tuple):
        if len(val) == 2:
            return SineWaveParam(val[0], val[1])
        elif len(val) == 3:
            return SineWaveParam(val[0], val[1], val[2])
        else:
            raise ValueError("Length of tuple of sine wave parameter must be 2 or 3")
    else:
        raise ValueError("Illegal parameter type")


class SineWave(Wave):
    def __init__(self, param: SineWaveParamType,
                *,
                duration: float,
                fs: int = 48000):
        assert duration > 0
        assert fs > 0

        self.param = _convert_param(param)
        self.duration = duration
        self.fs = fs

    def _generate_time_axis(self) -> np.ndarray:
        return np.linspace(
            0, self.duration, int(self.fs * self.duration), endpoint=False
        )

    def generate(self) -> np.ndarray:
        t = self._generate_time_axis()
        return self.param.amplitude * np.sin(2 * np.pi * self.param.frequency * t + self.param.phase)


class CompositeWave(Wave):
    def __init__(self, params: list[SineWaveParamType],
                 *,
                 duration: float,
                 fs: int = 48000):
        assert duration > 0
        assert fs > 0
        assert len(params) > 0

        self.params = list(map(lambda p: _convert_param(p), params))
        self.duration = duration
        self.fs = fs

    def _generate_time_axis(self) -> np.ndarray:
        return np.linspace(
            0, self.duration, int(self.fs * self.duration), endpoint=False
        )

    def generate(self) -> np.ndarray:
        sample_count = int(self.fs * self.duration)
        t = self._generate_time_axis()
        wave = np.zeros(sample_count)

        for param in self.params:
            w = param.amplitude * np.sin(2 * np.pi * param.frequency * t + param.phase)
            wave += w

        return wave
