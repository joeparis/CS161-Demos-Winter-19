#!/usr/bin/env python3
"""
Exercise the has_common_element() function from the mytools module.
"""
from random import randint
from mytools import filter_even as filter


def main():
    # test_data = []

    test_data = [randint(1, 10) for _ in range(15)]
    filtered_data = filter(test_data)
    print("{:16} {}".format("Test Data =", test_data))
    print("{:16} {}".format("Filtered Data =", filtered_data))
    print()


if __name__ == "__main__":
    main()
