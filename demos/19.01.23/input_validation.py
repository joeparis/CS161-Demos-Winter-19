#! /usr/bin/env python3
# coding=utf-8

"""
Demonstrates a method of getting and validating user input.
"""


def get_color_value(color, lower_limit=0.0, upper_limit=1.0):
    """
    Get a value for the color.

    Arguments:
        color {string} -- The name of the color value to get.
        lower_limit {float} -- The lower bound of the legal color value.
        upper_limit {float} -- The upper bound of the legal color value.

    Returns:
        float -- The color value.
    """
    # while True:
    #     value = float(input(f"Please enter the {color} value: "))
    #     if value >= 0 and value <= 1:
    #         break
    #     print(f"{value} is not valid, please enter a value betwen 0 and 1.")

    while True:
        try:
            value = float(input(f"Please enter the {color} value: "))
            if not (value >= lower_limit and value <= upper_limit):
                raise ValueError
            break
        except ValueError:
            print(
                f"Invalid input, please enter a number betwen {lower_limit} and {upper_limit}."
            )

    return value


def main():
    """
    Driver for demoing getting and validating user input for color values
    for turtle. Color values must be between >=0 and <=1.
    """

    red_value = get_color_value("red")
    green_value = get_color_value("green", 0.5, 1.0)
    blue_value = get_color_value("blue", 0.0, 0.6)

    print(red_value, green_value, blue_value)


if __name__ == "__main__":
    main()

