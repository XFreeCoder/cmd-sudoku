from textual.app import App
from textual.reactive import Reactive
from rich.align import Align
from textual.widgets import Footer, Placeholder, Static
from textual.widget import Widget


class TextWidget(Widget):

    def __init__(self, text: str, *, name: str=None):
        self.text = text
        super().__init__(name=name)

    def render(self):
        return  Align.center(self.text, vertical="middle")


class HelloWorld(App):
    """Demonstrates smooth animation. Press 'b' to see it in action."""

    async def on_mount(self) -> None:
        """Build layout here."""

        await self.view.dock(TextWidget("Hello World"))


HelloWorld.run(log="textual.log", log_verbosity=2)