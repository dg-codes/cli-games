import random
from os import name, system, wait
from time import sleep
from typing import Any


class BoardCell:
    value: str = "-"

    @property
    def is_empty(self):
        return self.value == "-"


def display_game_board(matrix: list[Any]) -> None:
    for i in range(3):
        for j in range(3):
            print(matrix[i * 3 + j], end=" ")
        print()


def check_winning_conditions(matrix: dict[str, Any], mark: str) -> bool:
    if (
        (matrix["A"] == matrix["B"] == matrix["C"] == mark)
        or (matrix["D"] == matrix["E"] == matrix["F"] == mark)
        or (matrix["G"] == matrix["H"] == matrix["I"] == mark)
        or (matrix["A"] == matrix["D"] == matrix["G"] == mark)
        or (matrix["B"] == matrix["E"] == matrix["H"] == mark)
        or (matrix["C"] == matrix["F"] == matrix["I"] == mark)
        or (matrix["A"] == matrix["E"] == matrix["I"] == mark)
        or (matrix["C"] == matrix["E"] == matrix["G"] == mark)
    ):
        return True
    return False


def is_game_finished(matrix: dict[str, Any]) -> bool:
    player_won = check_winning_conditions(matrix, "X")
    if player_won:
        print("\nYou win!")
        return True

    player_lost = check_winning_conditions(matrix, "O")
    if player_lost:
        print("\nYou lose!")
        return True

    board_filled = "-" not in list(matrix.values())
    if board_filled:
        print("\nIt's a tie!")
        return True

    return False


def run_game():
    matrix = {
        "A": "-",
        "B": "-",
        "C": "-",
        "D": "-",
        "E": "-",
        "F": "-",
        "G": "-",
        "H": "-",
        "I": "-",
    }

    display_game_board(list(matrix.keys()))
    print()
    display_game_board(list(matrix.values()))
    user_choice = None
    used_choices = set()
    while user_choice not in matrix.keys() or user_choice in used_choices:
        user_choice = input("Select a square (A to I): ").upper()
        if user_choice in matrix.keys():
            matrix[user_choice.upper()] = "X"
            used_choices.add(user_choice)

            available_options = [
                x for x in matrix.keys() if x not in used_choices
            ]
            ai_choice = random.choice(available_options)
            system("cls" if name == "nt" else "clear")
            display_game_board(list(matrix.keys()))
            print()
            display_game_board(list(matrix.values()))

            game_finished = is_game_finished(matrix)
            if game_finished:
                break

            sleep(0.5)
            matrix[ai_choice] = "O"
            used_choices.add(ai_choice)
        system("cls" if name == "nt" else "clear")
        display_game_board(list(matrix.keys()))
        print()
        display_game_board(list(matrix.values()))
        game_finished = is_game_finished(matrix)
        if game_finished:
            break
