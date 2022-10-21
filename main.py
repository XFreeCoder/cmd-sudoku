from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Placeholder, Static


class HelloWorld(App):
    """Demonstrates smooth animation. Press 'b' to see it in action."""

    async def on_mount(self) -> None:
        """Build layout here."""
        bar = Placeholder(name="Hello World")

        await self.view.dock(bar, z=1)


HelloWorld.run(log="textual.log", log_verbosity=2)