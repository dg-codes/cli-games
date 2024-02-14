from multiprocessing import Value

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
        with pytest.raises(ValueError) as value_error:
            cell = tic_tac_toe.BoardCell("A")


class TestGameBoard:
    @classmethod
    def test_is_full(cls):
        board = tic_tac_toe.GameBoard()
        board._matrix = {
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
        assert board.is_full
