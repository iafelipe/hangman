import os
import string
from time import sleep

from rich import box, print
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from draws import hangman

os.system("clear")
ALPHABET = [letter for letter in string.ascii_uppercase]

layout = Layout()
layout.split_row(Layout(name="left"), Layout(name="right"))
layout["right"].split_column(Layout(name="main"), Layout(name="prompt"))
layout["main"].split(Layout(name="top"), Layout(name="mid"), Layout(name="bot"))

layout["left"].size = 7
layout["prompt"].size = 4
layout["top"].size = 3
layout["bot"].size = 3

letters_grid = Table.grid()
letters_grid.add_column()
# for i in range(26):
#     letters_grid.add_row(f"{chr(i + 65)}")
letters_grid.add_row(" ".join(ALPHABET))

layout["left"].update(
    Panel(
        Align(letters_grid, align="center", vertical="middle"),
        box=box.SIMPLE,
    )
)

score_grid = Table.grid(expand=True)
score_grid.add_column()
score_grid.add_column(justify="right")
score_grid.add_row("SCORE: 12345", "[red]LIFES: 4")
layout["top"].update(Panel(score_grid, box=box.SIMPLE))

rules = Text(
    """Lorem ipsum dolor sit amet, consectetur 
    adipiscing elit. Cras et ligula est. Sed facilisis 
    tortor nunc, id tincidunt est condimentum et. 
    Suspendisse magna elit, tempus interdum turpis ut, 
    sollicitudin maximus diam. In non mattis risus.""",
    justify="center",
)

draw_grid = Table.grid(expand=True, padding=(0, 0, 0, 10))
draw_grid.add_column()
draw_grid.add_column()
draw_grid.add_row(
    hangman[6],
    Align(
        Panel(
            rules,
            title="Rules",
            width=30,
        ),
        vertical="middle",
    ),
)

layout["mid"].update(
    Panel(
        Align(draw_grid, vertical="middle", align="center"),
        title="HANGMAN",
        box=box.SIMPLE,
    )
)

word_progress = Text("A __ [green]C[/green] __ __ __ __")
layout["bot"].update(
    Panel(
        Align(word_progress, align="center"),
        box=box.SIMPLE,
    )
)

prompt_grid = Table.grid(expand=True)
prompt_grid.add_column()
prompt_grid.add_column(justify="right")
prompt_grid.add_row("", "reset [-r], bet [-b], quit [-q]")
prompt_grid.add_row("Enter a letter: ", "[red]ERROR")
layout["prompt"].update(Panel(prompt_grid, box=box.SIMPLE))

print(layout)

# try:
#     with Live(layout, refresh_per_second=4, screen=True):
#         sleep(100)
#     os.system("clear")

# except KeyboardInterrupt:
#     os.system("clear")
