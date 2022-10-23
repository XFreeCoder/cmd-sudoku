from widgets import CellWidget
from itertools import chain


class GamePlay():
    def __init__(self):
        self.widgets = [[
                        CellWidget() for _ in range(0, 9)
                        ] for _ in range(0, 9)]

    @property
    def flatten_widgets(self) -> list[CellWidget]:
        return list(chain.from_iterable(self.widgets))

    def generate_puzzle(self):
        for widget in self.flatten_widgets:
            widget.update_num(1)