import random
from os import name, system
from time import sleep
from typing import Any


class BoardCell:
    def __init__(self, value: str = "-") -> None:
        self._allowable_values = ["X", "O", "-"]
        self.value = value

    @property
    def value(self):
        return self._value

    @property
    def is_empty(self):
        return self._value == "-"

    def clear_value(self) -> str:
        """Set the `value` property back to the default `-`

        Returns
        -------
        str
            The default cells value of `-`.
        """
        self.value = "-"
        return self.value

    @value.setter
    def value(self, value: str) -> str:
        _new_value = value.upper()
        if _new_value not in self._allowable_values:
            raise ValueError(
                f"{value} is invalid. It should be either `X`, `O` or `-`."
            )

        self._value = value
        return self.value


class GameBoard:
    def __init__(self) -> None:
        self._matrix = {
            "A": BoardCell(),
            "B": BoardCell(),
            "C": BoardCell(),
            "D": BoardCell(),
            "E": BoardCell(),
            "F": BoardCell(),
            "G": BoardCell(),
            "H": BoardCell(),
            "I": BoardCell(),
        }

    @property
    def is_full(self):
        return len([x for x in self._matrix.values() if x.is_empty]) == 0

    def update_board(
        self, key: str, new_value: str, force_overwrite: bool = False
    ) -> dict[str, BoardCell]:
        if force_overwrite:
            self._matrix[key].value = new_value
            return self._matrix

        if self.is_full:
            print("There are no empty cells. Cannot update game board.")
            return self._matrix

        if self._matrix[key].is_empty is False:
            print("Cell is not empty. Try a different one.")
            return self._matrix

        self._matrix[key].value = new_value
        return self._matrix

    def get_board(self) -> dict[str, BoardCell]:
        return self._matrix


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
