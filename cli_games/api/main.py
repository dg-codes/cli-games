from os import getcwd, name, system
from pathlib import Path

from cli_games.core import hangman, number_guesser, tic_tac_toe
from cli_games.utils.file_manager import load_data


def run_app():
    user_input = None
    available_options = ["1", "2", "3"]
    while user_input not in available_options:
        system("cls" if name == "nt" else "clear")
        print(
            "Please select what you'd like to do:\n",
            "\t[1] Play Hangman\n",
            "\t[2] Play Number Guesser\n",
            "\t[3] Tic Tac Toe\n",
        )
        user_input = input()
    system("cls" if name == "nt" else "clear")
    if user_input == "1":
        current_directory = Path(getcwd())
        words = load_data(
            current_directory / "cli_games" / "data" / "hangman.txt"
        )
        game_settings = hangman.GameSettings(word_list=words)
        hangman.Hangman(game_settings).run_game()
    if user_input == "2":
        number_guesser.run_game(number_guesser.GameSettings())
    if user_input == "3":
        tic_tac_toe.run_game()
