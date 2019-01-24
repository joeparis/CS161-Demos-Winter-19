#! /usr/bin/python3
# coding=utf-8

"""
Demonstrates simple user input validation.

Below are examples of validating user input for type and range. Also shown
are examples of aborting the program on invalid input. This should be
avoided if at all possible and methods for re-prompting for valid input
should be used instead.
"""


def validate_integer_input():
    """
    Demonstrates validating that user input is an integer (does not validate
    that it is within any given range).
    """
    # isnumeric() simply checks if there are any non-digit characters in the
    # string and returns false if any are found.
    user_int = input("Please enter an integer: ")
    while not user_int.isnumeric():
        print("Invalid input. Please enter a valid integer value: ")
        user_int = input("Please enter an integer: ")

    return user_int


def validate_real_input():
    """
    Demonstrates validating that user input is a real (does not validate
    that it is within any given range).
    """
    # Because isnumeric() checks for any non-digit characters it fails on the
    # decimal place. We try to convert the user's input using float() which
    # raises an exception (which we then catch) on bad input.
    while True:
        user_real = input("Please enter a real number: ")
        try:
            user_real = float(user_real)
            break
        except ValueError:
            print("Invalid input. Please enter a valid real number: ")

    return user_real


def check_integer_range(lower=0, upper=100):
    """
    Demonstrates validating that user input is a number type within the
    specified range.

    Keyword Arguments:
        lower {int} -- The lower bound of the range (default: {0})
        upper {int} -- The  bound of the range (default: {100})
    """
    # We'll re-use the work we've already done to ensure what the user entered
    # was an integer by leveraging our integer validation function above.
    value = validate_integer_input()

    # If we get here we know value is an integer. Now, we check to make sure it
    # is in the required range.
    while True:
        if value >= lower and value < upper:
            break
        print(
            f"Please enter a value greater than or equal to {lower} and less than {upper}."
        )
        value = validate_integer_input()


def main():
    # demo validating that input is numeric (but not within a given range)
    print(validate_integer_input())
    print(validate_real_input())


if __name__ == "__main__":
    main()
