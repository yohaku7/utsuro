# """プロットできるものを表すインターフェース。"""
# import numpy as np
# import matplotlib.pyplot as plt
# from abc import ABC, abstractmethod
# from .plot_param import PlotParam


# class Plottable(ABC):
#     @abstractmethod
#     def _get_param(self) -> PlotParam:
#         pass

#     @abstractmethod
#     def _get_limits(self) -> tuple[tuple[float, float], tuple[float, float]]:
#         pass

#     def plot(self) -> None:
#         param = self._get_param()
#         t, y = self.get()

#         (x1, x2), (y1, y2) = self._get_limits()

#         plt.figure(figsize=(10, 6))
#         plt.xlim(x1, x2)
#         plt.ylim(y1, y2)
#         plt.title(param.title)
#         plt.xlabel(param.x_label)
#         plt.ylabel(param.y_label)
#         plt.tight_layout()
#         plt.plot(t, y)
#         plt.show()
