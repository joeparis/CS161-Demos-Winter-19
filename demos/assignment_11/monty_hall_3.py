#!/usr/bin/env python3
"""
The second part of the “Monty Hall Problem” is the most interesting. After
selecting a door, but before the prize door is revealed, the contestant is
shown a losing door. The contestant now has the option of switching to the
other, as-yet unopened door. Should the contestant stick with their original
choice, switch to the other unopened door, or does it not matter?

Modify your program from Part 1 to always choose to switch to the other door
and display the winning percentage after a large number of simulation runs.
"""
from random import choice, sample
from monty_hall_1 import all_doors
from monty_hall_2 import always_change


def random_change(verbose=False):
    """
    Simulate a single play of the Monty Hall Problem where, after a losing
    door is eliminated, the player has a 50/50 chance of changing their selected
    door.

    Keyword Arguments:
        verbose -- whether or not to display verbose output showing the result
            of every run (default: False)

    Returns:
        bool -- whether or not the contestant won
    """
    doors = ["Door #1", "Door #2", "Door #3"]
    doors_in_play = []

    prize_door = choice(doors)
    doors_in_play.append(prize_door)

    contestant_door = choice(doors)
    if contestant_door not in doors_in_play:
        doors_in_play.append(contestant_door)

    # if the contestant picked the winning door, choose another door at random
    # to add to the list of doors in play
    if len(doors_in_play) != 2:
        unchosen_doors = [
            door for door in doors if door not in (prize_door, contestant_door)
        ]
        doors_in_play.append(choice(unchosen_doors))

    # discard a door
    discarded_door = [door for door in doors if door not in doors_in_play][0]

    # 50/50 chance of swapping the contestant's door
    if choice([1, 2]) % 2 == 0:
        new_contestant_door = [
            door for door in doors_in_play if door not in contestant_door
        ][0]
    else:
        new_contestant_door = contestant_door

    winner = prize_door == new_contestant_door

    if verbose:
        print(
            f"You first chose {contestant_door}. We then eliminated {''.join(discarded_door)}. You switched to {''.join(new_contestant_door)}. The car was behind {prize_door}. ",
            end="",
        )
        if winner:
            print("YOU WIN!!!")
        else:
            print("Sorry, you lose. 😢😢😢")

    return winner


if __name__ == "__main__":
    RUNS = 10_000_000

    print()
    wins = 0
    for n in range(RUNS):
        wins += all_doors()
    print(
        f"With all doors in play, you win {wins:,} times out of {RUNS:,} runs, or {wins/RUNS*100:2.1f}% of the time."
    )

    wins = 0
    for n in range(RUNS):
        wins += always_change()
    print(
        f"With one door eliminated and your choice switched every time, you win {wins:,} times out of {RUNS:,} runs, or {wins/RUNS*100:2.1f}% of the time."
    )

    wins = 0
    for n in range(RUNS):
        wins += random_change()
    print(
        f"With one door eliminated and your choice switched 50% of the time, you win {wins:,} times out of {RUNS:,} runs, or {wins/RUNS*100:2.1f}% of the time."
    )
    print()
