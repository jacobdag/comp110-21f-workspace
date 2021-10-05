"""List utility functions part 2."""

__author__ = "730386191"


def only_evens(x: list[int]) -> list[int]:
    """Forms list of only even numbers."""
    i: int = 0
    y: list[int] = []
    while i < (len(x)):
        if (x[i] % 2) == 0:
            y.append(x[i])
        i += 1
    return (y)


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Forms subset list of given list."""
    i: int = 0
    new_list: list[int] = []
    while i < (len(a_list)):
        if x < 0:
            x = 0
        if a_list[i] == a_list[x] or ((a_list[i]) < a_list[y] and a_list[i] > a_list[x]):
            new_list.append(a_list[i])
        i += 1
    return (new_list)


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    new_list: list[int] = []
    for item in a_list:
        new_list.append(item)
    for item in b_list:
        new_list.append(item)
    return (new_list)