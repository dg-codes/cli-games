import random
from dataclasses import dataclass
from os import name, system

from cli_games.utils.life_support import LifeSupport


@dataclass
class GameSettings:
    word_list: list[str]
    total_lives: int = 10


def find_indexes_of_letter(string, letter):
    return [index for index, char in enumerate(string) if char == letter]


def display_word(letters: list[str]):
    print(" ".join(letters), end="\n")


def run_game(settings: GameSettings) -> None:
    print("You are playing HANGMAN!", end="\n")
    life_support = LifeSupport(settings.total_lives)
    selected_index = random.randint(0, len(settings.word_list) - 1)
    selected_word = settings.word_list[selected_index].lower()
    user_choices = set()
    word_display = ["_"] * len(selected_word)

    print([])
    display_word(word_display)

    while True:
        user_choice = None
        while user_choice not in user_choices:
            user_choice = input("Pick a letter: ").lower()
            system("cls" if name == "nt" else "clear")
            print("You are playing HANGMAN!", end="\n")
            if user_choice in user_choices:
                print(f"You have already used '{user_choice}'.", end="\n")
            else:
                user_choices.add(user_choice)

        indexes_to_change = find_indexes_of_letter(selected_word, user_choice)

        if len(indexes_to_change) > 0:
            for i in indexes_to_change:
                word_display[i] = user_choice
            life_support.display_lives()
        else:
            life_support.manage_hit()
            if life_support.is_dead:
                print(f"The word was '{selected_word}'!")
                break

        print(sorted(user_choices))
        display_word(word_display)

        if "_" not in word_display:
            print("Correct!", f"The word was '{selected_word}'.")
            break
