from utsuro.io import wavfile
from utsuro.signal import SineWave, SineWaveParam, CompositeWave
from utsuro.util import path

wave = CompositeWave(
    [
        (260,  0.1),
        (520,  0.1),
        (2860, 0.1),
        (3120, 0.1),
        (3380, 0.1),
    ],
    duration=1,
)

wavfile.write(path.get_tmp("i.wav"), wave)
