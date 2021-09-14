"""Finding duplicate letters in a word."""

__author__ = "730386191"

word: str = input("Enter a word: ")
i: int = 0
dup: bool = False

while i < len(word):
    char: str = word[i]
    j: int = i + 1
    while j < len(word):
        if word[j] == char:
            dup = True
        j = j + 1
    i = i + 1
print("Found duplicate:", dup)