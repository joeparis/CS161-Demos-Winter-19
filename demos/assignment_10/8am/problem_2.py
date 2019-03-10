#!/usr/bin/env python3
"""
Exercise the choose_random() function from the mytools module.
"""
import mytools


def main():
    my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(f"Random value from {my_tuple} : {mytools.choose_random(my_tuple)}")
    print()


if __name__ == "__main__":
    main()
