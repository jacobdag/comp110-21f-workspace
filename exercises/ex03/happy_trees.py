"""Drawing forests in a loop."""

__author__ = "730386191"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
depth_two: int = depth
i: int = 0
counter: int = 0


while counter < depth_two:
    print(TREE * int((depth - depth_two) + 1))
    depth = depth + 1
    counter = counter + 1
print()