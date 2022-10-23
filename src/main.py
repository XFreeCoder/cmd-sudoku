from textual.app import App
from textual.widgets import  Header, Footer, Static
from textual.containers import Container

from gameplay import GamePlay

class SudokuWidget(Static):

    def __init__(self):
        super().__init__()
        self.logic = GamePlay()
    
    def compose(self):
        yield Container(*self.logic.flatten_widgets)

    def on_mount(self):
        self.logic.generate_puzzle()    

class GameApp(App):
    CSS_PATH = "sudoku.css"

    def compose(self):
        yield Header()
        yield Footer()
        yield SudokuWidget()


if __name__ == "__main__":
    app = GameApp()
    app.run()
