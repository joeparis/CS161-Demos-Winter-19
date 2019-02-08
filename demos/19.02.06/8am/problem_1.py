#! /usr/bin/env python3
# coding=utf-8


def main():
    max_length = 0
    while True:
        current_word = input("Please enter a word: ")
        current_length = len(current_word)
        if current_length == 0:
            break
        max_length = max(current_length, max_length)
    print(f"the longest word entered had {max_length} characters.")


if __name__ == "__main__":
    main()
