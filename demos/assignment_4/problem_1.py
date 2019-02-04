#! /usr/bin/env python3
# coding=utf-8

"""
Write a Python function that prompts the user to enter any number of words
(end of input will be signified by their pressing ENTERon an empty line).
The program should display the length of the longest provided word.
"""


def main():
    max_length = 0
    while True:
        current_word = input("Please enter a word: ")
        current_length = len(current_word)
        if current_length == 0:
            break
        max_length = max(current_length, max_length)
    print(f"The longest word entered had {max_length} characters.")


if __name__ == "__main__":
    main()
