import random
import string


def pick_word(words_file):
    with open(words_file, "r", encoding="utf-8") as f:
        words = f.read().split("\n")
        return random.choice(words)


def find_indices(char, word):
    index = -1
    while True:
        index = word.find(char, index + 1)
        if index == -1:
            break
        yield index


def is_valid(char):
    if char in string.ascii_letters:
        return True
    else:
        return False


def main():
    # word = pick_word("words.tchart")
    wrong_guesses = 0
    right_guesses = 0
    word = "radiant"
    length = len(word)
    guess = ["__,"] * length

    while True:
        print(guess, "\n")

        if wrong_guesses == 6:
            print("You lost!")
            break

        if right_guesses == length:
            print("You win!")
            break

        char = input("Insert a letter: ")
        if is_valid(char):
            if char in guess:
                print("You've already enter this letter, select another one\n")

            else:
                if char in word:
                    print("You find a word!\n")
                    for i in find_indices(char, word):
                        guess[i] = char
                        right_guesses += 1

                else:
                    print("-1 body part\n")
                    wrong_guesses += 1

        else:
            print("Please enter a valid letter\n")


if __name__ == "__main__":
    main()
