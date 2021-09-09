"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730386191"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint

print("Your fortune cookie says... ")

cookie: int = (randint(1, 4))
if cookie == 1:
    print("The coming week will be a good one.")
else: 
    if cookie == 2:
        print("An old friend will find you again.")
    else:
        if cookie == 3:
            print("Good times are approaching.")
        else:
            print("Wealth and happiness will soon find you.")

print("Now, go spread positive vibes!")
