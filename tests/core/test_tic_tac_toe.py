import pytest

from cli_games.core import tic_tac_toe


def test_set_value():
    cell = tic_tac_toe.BoardCell()
    expected = "A"
    assert cell.set_value(value="A") == expected


def test_is_empty():
    cell = tic_tac_toe.BoardCell()
    assert cell.is_empty is True
