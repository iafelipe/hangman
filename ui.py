import os
import string

from rich import box
from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from draws import hangman

word = "radiant"
length = len(word)
guess = ["__"] * length
guess[0] = "R"
guess[2] = "D"
guess[6] = "T"

ALPHABET = [letter for letter in string.ascii_uppercase]
stddict = {c: c for c in ALPHABET}

letters = " ".join(stddict.values())

layout = Layout()
console = Console()

layout.split(Layout(name="header"), Layout(name="main"))
layout["header"].size = 4
layout["main"].split_row(Layout(name="left"), Layout(name="right"))

layout["left"].split(Layout(name="draw"))
layout["right"].split(Layout(name="scores"), Layout(name="rules"))
layout["scores"].size = 5

layout["header"].update(
    Panel(
        Align(
            Text.from_markup(" ".join(stddict.values())),
            align="center",
            vertical="bottom",
        ),
        box=box.SIMPLE,
    )
)

draw_grid = Table.grid(expand=True)
draw_grid.add_column()
draw_grid.add_row(hangman[6])
draw_grid.add_row("\n")
draw_grid.add_row(Text(" ".join(guess), justify="center"))

layout["draw"].update(
    Panel(
        Align(
            draw_grid,
            align="center",
            vertical="top",
        ),
        box=box.SIMPLE,
    )
)

layout["rules"].update(
    Panel(
        Panel(
            Align(
                Text(
                    """Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Cras et ligula est. Sed facilisis
    tortor nunc, id tincidunt est condimentum et.
    Suspendisse magna elit, tempus interdum turpis ut,
    sollicitudin maximus"""
                ),
                align="center",
                vertical="middle",
            ),
            padding=(0, 2),
            title="Rules",
        ),
        padding=(0, 5, 2, 5),
        box=box.SIMPLE,
    )
)

scores_grid = Table.grid(expand=True)
scores_grid.add_column(justify="center")
scores_grid.add_row(" [red]* " * 5)
scores_grid.add_row("")
scores_grid.add_row("[green]SCORE:[/green] 123345")

layout["scores"].update(
    Panel(
        Align(
            scores_grid,
            align="center",
            vertical="middle",
        ),
        box=box.SIMPLE,
    )
)

prompt_grid = Table.grid(expand=True)
prompt_grid.add_column()
prompt_grid.add_column(justify="right")
prompt_grid.add_row("[grey]reset [-r], bet [-b], quit [-q][/grey]", "")
prompt_grid.add_row("", "")
prompt_grid.add_row("a", "Invalid prompt!")

console.print(layout)
console.input(" > Enter a letter: ")
os.system("clear")

console.print(layout)
console.input(" > Enter a letter: ")
os.system("clear")
