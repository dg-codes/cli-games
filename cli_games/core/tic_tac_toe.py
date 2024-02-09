from os import name, system
from typing import Any


def display_game_board(matrix: list[Any]) -> None:
    for i in range(3):
        for j in range(3):
            print(matrix[i * 3 + j], end=" ")
        print()


def check_winning_conditions(matrix: dict[str, Any], mark: str) -> bool:
    if (
        (matrix["A"] == matrix["B"] == matrix["C"] == mark)
        or (matrix["A"] == matrix["D"] == matrix["G"] == mark)
        or (matrix["A"] == matrix["E"] == matrix["I"] == mark)
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

    board_filled = 0 not in list(matrix.values())
    if board_filled:
        print("\nIt's a tie!")
        return True

    return False


def run_game():
    matrix = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
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

        system("cls" if name == "nt" else "clear")
        display_game_board(list(matrix.keys()))
        print()
        display_game_board(list(matrix.values()))
        game_finished = is_game_finished(matrix)
        if game_finished:
            break