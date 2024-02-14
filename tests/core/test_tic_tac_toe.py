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
