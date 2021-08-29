"""Bool numeric comparisons."""

__author__ = "730386191"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

less_than: bool = (left_hand_side < right_hand_side)
print(left_hand_side, "<", right_hand_side, "is", less_than)

greater_equal: bool = (left_hand_side >= right_hand_side)
print(left_hand_side, ">=", right_hand_side, "is", greater_equal)

equal_to: bool = (left_hand_side == right_hand_side)
print(left_hand_side, "==", right_hand_side, "is", equal_to)

not_equal_to: bool = (left_hand_side != right_hand_side)
print(left_hand_side, "!=", right_hand_side, "is", not_equal_to)
