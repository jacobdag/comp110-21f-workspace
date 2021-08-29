"""Numeric functions operation."""

_author_ = "730386191"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

multiply: int = (left_hand_side ** right_hand_side)
print(left_hand_side, "**", right_hand_side, "is", multiply)

divide: float = (left_hand_side / right_hand_side)
print(left_hand_side, "/", right_hand_side, "is", divide)

int_divide = int(left_hand_side // right_hand_side)
print(left_hand_side, "//", right_hand_side, "is", int_divide)

remainder = int(left_hand_side % right_hand_side)
print(left_hand_side, "%", right_hand_side, "is", remainder)
