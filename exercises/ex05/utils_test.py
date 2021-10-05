"""Unit tests for list utility functions."""


__author__ = "730386191"

from exercises.ex05.utils import only_evens, sub, concat


# Only even tests.
def test_only_evens() -> None:
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


def test_only_evens_random() -> None:
    x: list[int] = [2, 5, 4, 6, 7, 10, 12, 14]
    assert only_evens(x) == [2, 4, 6, 10, 12, 14]


def test_only_evens_no_input() -> None:
    x: list[int] = []
    assert only_evens(x) == []


# Sub Tests.
def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    x: int = 1
    y: int = 3
    assert sub(a_list, x, y) == [20, 30]


def test_sub_large() -> None:
    a_list: list[int] = [10, 11, 12, 13, 14, 15, 16, 17]
    x: int = 2
    y: int = 6
    assert sub(a_list, x, y) == [12, 13, 14, 15]


def test_sub_over_under() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    x: int = -1
    y: int = 3
    assert sub(a_list, x, y) == [10, 20, 30]


# Concat tests.
def test_concat() -> None:
    a_list: list[int] = [1, 2, 3, 4]
    b_list: list[int] = [5, 6, 7, 8]
    assert concat(a_list, b_list) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_small() -> None:
    a_list: list[int] = [1, 2]
    b_list: list[int] = [4, 7, 8]
    assert concat(a_list, b_list) == [1, 2, 4, 7, 8]


def test_concat_no_input() -> None:
    a_list: list[int] = [1, 2, 3, 4]
    b_list: list[int] = []
    assert concat(a_list, b_list) == [1, 2, 3, 4]