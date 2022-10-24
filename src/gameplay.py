from sudoku import generate_puzzle
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
        puzzle = generate_puzzle()
        for index, digit in enumerate(puzzle.values()):
            self.flatten_widgets[index].update_num(
                int(digit) if len(digit) == 1 else 0)
