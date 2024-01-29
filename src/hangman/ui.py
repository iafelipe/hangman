from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .draws import hangman


def display(
    console: Console, wrong_guesses: int, guess: list, rich_letters: dict
) -> None:
    panel = Panel(Align(Text(hangman[wrong_guesses]), align="center"), box=box.SIMPLE)

    grid = Table.grid(expand=True)
    grid.add_column()
    grid.add_row("\n")
    grid.add_row(Text.from_markup(" ".join(rich_letters.values()), justify="center"))
    grid.add_row(panel)
    grid.add_row(Text(" ".join(guess), justify="center"))
    grid.add_row()

    console.print(grid)
