#!/usr/bin/env python3
"""
Exercise the has_common_element() function from the mytools module.
"""
from mytools import has_common_element


def main():
    test_data_1 = [1, 2, 3, 4, 5]
    test_data_2 = [5, 6, 7, 8, 9]
    print(
        f"{test_data_1} and {test_data_2} have at least one common element? : {has_common_element(test_data_1, test_data_2)}"
    )
    test_data_3 = [0, 1, 2, 3, 4]
    test_data_4 = [5, 6, 7, 8, 9]
    print(
        f"{test_data_3} and {test_data_4} have at least one common element? : {has_common_element(test_data_3, test_data_4)}"
    )
    print()


if __name__ == "__main__":
    main()
