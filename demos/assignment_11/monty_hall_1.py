#!/usr/bin/env python3
"""
The “Monty Hall Problem” (https://en.wikipedia.org/wiki/Monty_Hall_problem) is
a classic introduction to game theory and probability simulations that comes
from a live TV game show in the 1960s. A contestant is faced with three doors.
Behind one door is a very large prize (say, a car). The contestant tries to
guess which door has the prize. We already know that mathematically the
contestant should win 33% of the time. Write a program that uses a Monte Carlo
simulation to prove it. For each simulation run, the program should use a
variable to represent the randomly chosen winning door number. The program
should then randomly select a door number from one to three to represent the
contestant’s choice. Finally, display the winning percentage after a large
number of simulation runs, and confirm that it is very close to 33%.
"""
from random import choice


def all_doors(verbose=False):
    """
    Simulate a single play of a simplified version of the Monty Hall Problem
    where all three doors are always in play.

    Keyword Arguments:
        verbose -- whether or not to display verbose output showing the result
            of every run (default: False)

    Returns:
        bool -- whether or not the contestant won
    """
    doors = ["Door #1", "Door #2", "Door #3"]
    prize_door = choice(doors)
    contestant_door = choice(doors)
    winner = prize_door == contestant_door

    if verbose:
        print(
            f"You choose {contestant_door}, the car was behind {prize_door}. ", end=""
        )
        if winner:
            print("YOU WIN!!!")
        else:
            print("Sorry, you lose. 😢😢😢")

    return winner


if __name__ == "__main__":
    RUNS = 10_000_000
    wins = 0
    for n in range(RUNS):
        wins += all_doors()
    print(
        f"You won {wins:,} times out of {RUNS:,} runs, or {wins/RUNS*100:2.1f}% of the time.\n"
    )
