#!/usr/bin/env python3
"""
Simple utility library to demonstrate importing and using functions from a
module.
"""
from random import choice, randint, randrange


def create_random_tuple():
    """
    Return a tuple with length between 10 and 20 (inclusive), populated with
    random integers between 1 and 100 (inclusive).
    """
    return tuple([randint(1, 100) for _ in range(randrange(10, 21))])


def choose_random(values):
    """
    Return a random value from the tuple passed as an argument.
    """
    return choice(values)


def has_common_element(a, b):
    """
    Return True if iterables a and b have at least one element in common.
    """
    return not len(set(a) & set(b)) == 0


def filter_even(l):
    """
    Return a new list consisting of the members of l that are odd.
    """
    return [num for num in l if num % 2 != 0]


if __name__ == "__main__":
    print("Exercising create_random_tuple()")
    t = create_random_tuple()
    print(f"{type(t)} {t}")
    print()
    print("Exercising choose_random()")
    print(choose_random(t))
    print()
    print("Imagine has_common_element() and filter_even() being exercised here...")
    print()

