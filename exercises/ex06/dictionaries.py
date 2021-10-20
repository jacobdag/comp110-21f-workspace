"""Practice with dictionaries."""

__author__ = "730386191"


def invert(set: dict[str, str]) -> dict[str, str]:
    """Inverts key and value."""
    inverted_set = dict()
    for key in set:
        value = set[key]
        inverted_set[value] = key
    return(inverted_set)


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most common color."""
    i = 0
    count = 0
    maximum = 0
    list_key = list()
    final_max = ""
    for key in colors:
        list_key.append(colors[key])
    for item in list_key:
        while i < len(list_key) - 1:
            if list_key[i] == item:
                count += 1
                i += 1
                if count >= maximum:
                    maximum = count
                    final_max = item
    return(final_max)        


def count(list_one: list[str]) -> dict[str, int]:
    """Count the value."""
    new_dict = dict()
    for item in list_one:
        if item in new_dict:
            new_dict[item] += 1
        else: 
            new_dict[item] = 1
    return(new_dict)