"""List utility functions."""


__author__ = "730386191"


def all(numbers: list[int], search: int) -> bool:
    """Returns True for list all specific int."""
    i: int = 0
    counter: int = 0
    while i < len(numbers):
        item: int = numbers[i]
        i += 1 
        if item == search:
            counter += 1
    if counter == len(numbers):
        return True 
    return False


def is_equal(group: list[int], group_two: list[int]) -> bool:
    """True if matching lists."""
    i: int = 0
    counter: int = 0
    while i < len(group) and len(group_two):
        i += 1
        if group == group_two:
            counter += 1
    if counter == i and len(group) == len(group_two):
        return True
    return False


def max(input: list[int]) -> int:
    """Returns max number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        i: int = 0
        maximum: int = 0
        while i < (len(input) - 1):
            item: int = input[i]
            item_two: int = (input[i + 1])
            if item <= item_two and item_two >= input[0]:
                maximum = item_two
            else:
                maximum = input[0]
            if item == maximum:
                maximum = item
            i += 1
    return (maximum)
