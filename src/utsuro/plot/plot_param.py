"""プロットするときに使用するパラメータ。"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PlotParam:
    title: str
    x_label: str
    y_label: str
