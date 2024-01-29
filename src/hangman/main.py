import os
import random
import string
from collections.abc import Iterable

from rich.console import Console
from rich.prompt import Confirm, Prompt

from .ui import display

ALPHABET = [letter for letter in string.ascii_uppercase]


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def search_char(char: str, word: str) -> Iterable[int]:
    index = -1
    while True:
        index = word.find(char, index + 1)
        if index == -1:
            break
        yield index


def main() -> None:
    try:
        console = Console()

        with open("words.txt", "r", encoding="utf-8") as f:
            possible_words = f.read().splitlines()

            while True:
                word = random.choice(possible_words).upper()
                guess = ["__"] * len(word)
                wrong_letters = []
                rich_letters = {c: c for c in ALPHABET}

                count_wrong = 0
                count_right = 0
                valid_char = True
                repeated_letter = False

                while True:
                    clear_screen()
                    display(console, count_wrong, guess, rich_letters)

                    if count_wrong == 6:
                        console.print("[red]You lost! :cry::2nd_place_medal:")
                        break

                    if count_right == len(word):
                        console.print("[green]You win! :smiley::1st_place_medal:")
                        break

                    if not valid_char:
                        console.print("[prompt.invalid]Please enter a valid letter!")

                    if repeated_letter:
                        console.print(
                            "[prompt.invalid]You've already entered this letter!"
                        )

                    char = Prompt.ask("Insert a letter [cyan](-q to quit)").upper()

                    if char == "-Q":
                        break

                    valid_char = char in ALPHABET

                    if valid_char:
                        if char in guess or char in wrong_letters:
                            repeated_letter = True

                        else:
                            if char in word:
                                for i in search_char(char, word):
                                    count_right += 1
                                    guess[i] = char
                                    rich_letters[
                                        char
                                    ] = f"[bold green]{char}[/bold green]"

                            else:
                                count_wrong += 1
                                wrong_letters.append(char)
                                rich_letters[char] = f"[bold red]{char}[/bold red]"

                restart = Confirm.ask("Wanna play again?", default=True)
                if not restart:
                    break

                clear_screen()

    except KeyboardInterrupt:
        console.print(" [yellow]See you later! :wave::smiley:")


if __name__ == "__main__":
    main()
