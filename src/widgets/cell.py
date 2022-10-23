
from textual.widgets import Static
from textual.reactive import Reactive


class CellWidget(Static):
  num = Reactive(0)

  def update_num(self, num):
    self.num = num

  def watch_num(self, num: int) -> None:
    self.update(str(num) if num > 0 else "")

  def render(self):
    return str(self.num)