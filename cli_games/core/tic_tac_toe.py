import random
from os import name, system
from time import sleep


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
        return len(self.get_available_options()) == 0

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

    def get_available_options(self) -> list[str]:
        available_moves = [
            cell_name
            for cell_name, cell_value in self._matrix.items()
            if cell_value.is_empty
        ]
        return available_moves

    def get_board(self) -> dict[str, BoardCell]:
        return self._matrix

    def display_game_board(self) -> None:
        board_display = [cell.value for cell in self._matrix.values()]
        self._display_matrix(board_display)

    def display_game_board_help(self) -> None:
        board_display = list(self._matrix.keys())
        self._display_matrix(board_display)

    def _display_matrix(self, matrix: list[str]) -> None:
        for i in range(3):
            for j in range(3):
                print(matrix[i * 3 + j], end=" ")
            print()

    def check_winning_conditions(self, mark: str) -> bool:
        if (
            (
                self._matrix["A"].value
                == self._matrix["B"].value
                == self._matrix["C"].value
                == mark
            )
            or (
                self._matrix["D"].value
                == self._matrix["E"].value
                == self._matrix["F"].value
                == mark
            )
            or (
                self._matrix["G"].value
                == self._matrix["H"].value
                == self._matrix["I"].value
                == mark
            )
            or (
                self._matrix["A"].value
                == self._matrix["D"].value
                == self._matrix["G"].value
                == mark
            )
            or (
                self._matrix["B"].value
                == self._matrix["E"].value
                == self._matrix["H"].value
                == mark
            )
            or (
                self._matrix["C"].value
                == self._matrix["F"].value
                == self._matrix["I"].value
                == mark
            )
            or (
                self._matrix["A"].value
                == self._matrix["E"].value
                == self._matrix["I"].value
                == mark
            )
            or (
                self._matrix["C"].value
                == self._matrix["E"].value
                == self._matrix["G"].value
                == mark
            )
        ):
            return True
        return False

    def is_game_finished(self) -> bool:
        player_won = self.check_winning_conditions("X")
        if player_won:
            print("\nYou win!")
            return True

        player_lost = self.check_winning_conditions("O")
        if player_lost:
            print("\nYou lose!")
            return True

        if self.is_full:
            print("\nIt's a tie!")
            return True

        return False


def run_game():
    game_board = GameBoard()
    game_board.display_game_board_help()
    print()
    game_board.display_game_board()
    user_choice = None
    available_options = game_board.get_available_options()
    while user_choice not in available_options:
        user_choice = input("Select a square (A to I): ").upper()
        if user_choice in available_options:
            game_board.update_board(user_choice.upper(), "X")
            available_options = game_board.get_available_options()
            ai_choice = random.choice(available_options)
            system("cls" if name == "nt" else "clear")
            game_board.display_game_board_help()
            print()
            game_board.display_game_board()

            game_finished = game_board.is_game_finished()
            if game_finished:
                break

            sleep(0.5)
            game_board.update_board(ai_choice, "O")
        system("cls" if name == "nt" else "clear")
        game_board.display_game_board_help()
        print()
        game_board.display_game_board()
        game_finished = game_board.is_game_finished()
        if game_finished:
            break
