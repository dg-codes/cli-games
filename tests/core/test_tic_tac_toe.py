import pytest

from cli_games.core import tic_tac_toe


class TestBoardCell:
    @classmethod
    def test_set_value(cls):
        cell = tic_tac_toe.BoardCell()
        expected = "X"
        cell.value = "X"
        assert cell.value == expected

    @classmethod
    def test_is_empty_True(cls):
        cell = tic_tac_toe.BoardCell()
        assert cell.is_empty is True

    @classmethod
    def test_is_empty_False(cls):
        cell = tic_tac_toe.BoardCell("X")
        assert cell.is_empty is False

    @classmethod
    def test_constructor_setter(cls):
        with pytest.raises(ValueError):
            tic_tac_toe.BoardCell("A")


@pytest.fixture
def game_board() -> tic_tac_toe.GameBoard:
    game_board = tic_tac_toe.GameBoard()
    game_board._matrix = {
        "A": tic_tac_toe.BoardCell("X"),
        "B": tic_tac_toe.BoardCell("X"),
        "C": tic_tac_toe.BoardCell("X"),
        "D": tic_tac_toe.BoardCell("X"),
        "E": tic_tac_toe.BoardCell("X"),
        "F": tic_tac_toe.BoardCell("X"),
        "G": tic_tac_toe.BoardCell("X"),
        "H": tic_tac_toe.BoardCell("X"),
        "I": tic_tac_toe.BoardCell("X"),
    }
    return game_board


class TestGameBoard:
    def test_is_full(self, game_board: tic_tac_toe.GameBoard):
        assert game_board.is_full

    def test_board_should_not_update(self, game_board: tic_tac_toe.GameBoard):
        game_board.update_board("A", "O")
        _board_values = set(
            [entry.value for entry in game_board._matrix.values()]
        )
        assert "O" not in _board_values

    def test_board_should_update(self, game_board: tic_tac_toe.GameBoard):
        game_board.update_board("A", "O", True)
        _board_values = set(
            [entry.value for entry in game_board._matrix.values()]
        )
        assert "O" in _board_values
