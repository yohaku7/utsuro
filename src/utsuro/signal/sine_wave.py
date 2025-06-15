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
        self._duration = duration
        self._fs = fs

    def generate(self) -> np.ndarray:
        t = self.generate_time_axis()
        return self.param.amplitude * np.sin(2 * np.pi * self.param.frequency * t + self.param.phase)

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def fs(self) -> int:
        return self._fs


class CompositeWave(Wave):
    def __init__(self, params: list[SineWaveParamType],
                 *,
                 duration: float,
                 fs: int = 48000):
        assert duration > 0
        assert fs > 0
        assert len(params) > 0

        self.params = list(map(lambda p: _convert_param(p), params))
        self._duration = duration
        self._fs = fs

    def generate(self) -> np.ndarray:
        sample_count = int(self._fs * self._duration)
        t = self.generate_time_axis()
        wave = np.zeros(sample_count)

        for param in self.params:
            w = param.amplitude * np.sin(2 * np.pi * param.frequency * t + param.phase)
            wave += w

        return wave

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def fs(self) -> int:
        return self._fs
