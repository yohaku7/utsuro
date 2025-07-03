# """ケプストラム。"""
# # refer: https://nettyukobo.com/cepstrum/
# import numpy as np
# import matplotlib.pyplot as plt
# from utsuro.signal import Wave
# from utsuro.signal.window import apply_window


# class Cepstrum:
#     def __init__(self, wave: Wave, start: int = 100, N: int = 2 ** 14):
#         assert start >= 0
#         assert N >= 4096, "標本点数が少なすぎます。"

#         self.wave = wave
#         self.start = start
#         self.N = N

#     def get(self) -> tuple[np.ndarray, np.ndarray]:
#         data = self.wave.generate()

#         # 範囲指定
#         data = data[self.start:self.start+self.N]

#         # 窓
#         data = apply_window(data, "hanning", correction=True)

#         fft = np.fft.rfft(data)

#         # 対数変換
#         fft = np.abs(fft)
#         fft = np.log10(fft + 1e-9)

#         # ケフレンシ軸 [ms]
#         ceps_t = np.arange(self.N) * 1000 / self.wave.fs
#         # ケプストラム
#         ceps = np.fft.irfft(fft)

#         return ceps_t, ceps
    
#     def _get_lifter_threshold(self) -> np.signedinteger:
#         # 基本周期を推定し、その半分までをリフタリングの閾値とする
#         _, ceps = self.get()

#         To_low = self.wave.fs // 800
#         To_high = self.wave.fs // 40
#         To = np.argmax(ceps[To_low:To_high]) + To_low
#         lifter = To // 2

#         return lifter

#     def get_spectrum_envelope(self) -> np.ndarray:
#         _, ceps = self.get()

#         # リフタリング
#         lifter = self._get_lifter_threshold()
#         ceps[:lifter] = 0
#         ceps[self.N-lifter+1:] = 0

#         envelope = np.real(np.fft.rfft(ceps))
#         return envelope

#     def get_spectral_fine_component(self) -> np.ndarray:
#         _, ceps = self.get()

#         # リフタリング
#         lifter = self._get_lifter_threshold()
#         ceps[lifter:self.N-lifter+1] = 0

#         fine = np.real(np.fft.rfft(ceps))
#         return fine


# def plot(wave: Wave) -> None:
#     data = wave.generate()

#     # 基本周波数の推定
#     To_low = wave.fs // 800
#     To_high = wave.fs // 40
#     ylim = np.max(ceps[To_low:To_high])

#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     # ax.set_xlim(0, 30)
#     # ax.set_ylim(-0.02, ylim + 0.02)
#     ax.set_xlabel("Quefrency [ms]")
#     ax.set_ylabel("Log Amplitude")
#     ax.plot(ceps_t, ceps, c="red")

#     plt.xlim(0, 4000)
#     # plt.ylim(-50, -10)
#     plt.xlabel("Frequency [Hz]")
#     plt.ylabel("Amplitude [dB]")
#     plt.plot(freq, 10 * fft, c="red")
#     plt.plot(freq, 10 * envelope, c="blue")
#     plt.show()

#     return envelope
