"""Guessing Game Gamble."""

__author__ = "730386191"


player: str = input("Hello, what is your name? ") 
points = int()


def greet() -> None:
    """Greet."""
    global player
    name = str(player)
    emoji_one: str = "\U0001F608"
    print(f"- Hello {name}, welcome to the Number Gambling Guessing Game {emoji_one}!")
    print("- The objective of this game is to guess what number, from 1-3, or 10-20 (for a greater challenge), will be called.")
    print("- You will enter your guess by typing it when prompted.")
    print("- The number of correct guesses in a row will be tallied.")
    print(f"- Try and quit with the highest streak possible. Like all gambling, this is a game of risks {emoji_one}!!!")


def main() -> None:
    """Entry."""
    global player
    name: str = player
    guess_loop: int = int(input(f"{name}, to guess from 1-3, type '3'. To guess from 10-20, type '10'. To quit, enter '0'. Good luck {name}!: "))
    if guess_loop == 3:    
        x: int = (int(input(("Enter a number from 1-3 to guess: "))))
        guess(x)
    if guess_loop == 10:
        y: int = (int(input(("Enter a number from 10-20 to guess: "))))
        guess_ten(y)
    if guess_loop == 0:
        ending(points)


def guess(x: int) -> None:
    """Guessing to 3."""
    from random import randint
    answer: int = randint(1, 3)
    if int(x) == int(answer):
        global points
        points = points + 1
        print(f"Correct, you have guessed {points} in a row!!!")
        main()
    else:
        print(f"{x} is wrong, the answer was {answer}. You have no guessing streak")
        points = 0
        main()


def guess_ten(y: int) -> None:
    """Guessing 10 to 20."""
    from random import randint
    answer: int = randint(10, 20)
    if int(y) == int(answer):
        global points
        points = points + 1
        print(f"Correct, you have guessed {points} in a row!!!")
        main()
    else:
        print(f"{y} is wrong, the answer was {answer}. You have no guessing streak!!!")
        points = 0
        main()


def ending(points: int) -> None:   
    emoji_two: str = "\U0001F928"
    emoji_three: str = "\U0001F61E"
    emoji_four: str = "\U0001F60E"
    if points <= 1:
        print(f"Game Over {player}, looks like you gambled too much {emoji_two}, or perhaps not enough... You ended with no real streak {emoji_three}")
    if points > 1:
        print(f"Congrats {player} on choosing to end with a streak of {points}. Better safe than sorry {emoji_four}!")


if __name__ == "__main__":
    greet()
    main()