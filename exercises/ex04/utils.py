"""List utility functions."""

__author__ = "123456789"


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
    if counter == i:
        return True
    return False


def max(input: list[int]) -> int:
    """Returns max number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    while i < len(input):
        label: int = input[i]
        i += 1
        if label >= input[i]:
            maximum: int = label
    return maximum
