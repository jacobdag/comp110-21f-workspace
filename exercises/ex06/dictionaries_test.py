"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count


__author__ = "730386191"


def test_invert() -> None:
    """Standard use invert dictionary characters."""
    set: dict = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(set) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words() -> None:
    """Standard use invert dictionary characters."""
    set: dict = {'Monster': 'Cookie', 'Dog': 'Cat', 'Then': 'Ok'}
    assert invert(set) == {'Cookie': 'Monster', 'Cat': 'Dog', 'Ok': 'Then'}


def test_invert_none() -> None:
    """No input."""
    set: dict = {'': ''}
    assert invert(set) == {'': ''}


def test_favorite_color_small() -> None:
    """Standard use small sample."""
    colors: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_large() -> None:
    """Standard use large sample."""
    colors: dict = {"J": "Purple", "A": "Green", "K": "Teal", "M": "Teal", "F": "Purple", "G": "Teal"}
    assert favorite_color(colors) == "Purple"


def test_favorite_color_tie() -> None:
    """Tie Scenario."""
    colors: dict = {"J": "Purple", "K": "Teal", "M": "Teal", "F": "Purple"}
    assert favorite_color(colors) == "Purple"


def test_no_repeats() -> None:
    """No repeats."""
    list_one: list = ["j", "a", "k", "e"]
    assert count(list_one) == {"j": 1, "a": 1, "k": 1, "e": 1}


def test_repeats() -> None:
    """Repeats."""
    list_one: list = ["j", "j", "a", "a"]
    assert count(list_one) == {"j": 2, "a": 2}


def test_repeat_once() -> None:
    """One repeat."""
    list_one: list = ["j", "j", "a", "k", "e"]
    assert count(list_one) == {"j": 2, "a": 1, "k": 1, "e": 1}