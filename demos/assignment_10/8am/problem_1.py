#!/usr/bin/env python3
"""
Exercise the create_random_tuple() function from the mytools module.
"""
import mytools


def main():
    print("Creating random tuple with create_random_tuple()...>=🦄")
    my_tuple = mytools.create_random_tuple()
    print(f"my_tuple is of type {type(my_tuple)}")
    print(len(my_tuple))
    print(my_tuple)
    print()


if __name__ == "__main__":
    main()
