import random
from dataclasses import dataclass
from os import name, system

from cli_games.utils.life_support import LifeSupport


@dataclass
class GameSettings:
    word_list: list[str]
    total_lives: int = 10


class Hangman:
    def __init__(self, game_settings: GameSettings) -> None:
        self._settings = game_settings
        self._selected_word = None
        self._word_display = None

    def find_indexes_of_letter(self, letter):
        return [
            index
            for index, char in enumerate(self._selected_word)
            if char == letter
        ]

    def display_word(self):
        print(" ".join(self._word_display), end="\n")

    def run_game(self) -> None:
        print("You are playing HANGMAN!", end="\n")
        life_support = LifeSupport(self._settings.total_lives)
        selected_index = random.randint(0, len(self._settings.word_list) - 1)
        self._selected_word = self._settings.word_list[selected_index].lower()
        user_choices = set()
        self._word_display = ["_"] * len(self._selected_word)

        print([])
        self.display_word()

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

            indexes_to_change = self.find_indexes_of_letter(user_choice)

            if len(indexes_to_change) > 0:
                for i in indexes_to_change:
                    self._word_display[i] = user_choice
                life_support.display_lives()
            else:
                life_support.manage_hit()
                if life_support.is_dead:
                    print(f"The word was '{self._selected_word}'!")
                    break

            print(sorted(user_choices))
            self.display_word()

            if "_" not in self._word_display:
                print("Correct!", f"The word was '{self._selected_word}'.")
                break
