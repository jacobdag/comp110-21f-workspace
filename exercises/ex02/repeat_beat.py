"""Repeating a beat in a loop."""

__author__ = "730386191"


beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want me to repeat it? "))
i: int = 0
repeat_two: int = repeat
beat_multi: str = (str(beat + " ") * int(repeat))

while i >= repeat:
    print("No beat...")
    repeat = i + 1

while i < repeat_two:
    print(beat_multi)
    repeat_two = i