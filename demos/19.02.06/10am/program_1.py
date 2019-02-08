#! /usr/bin/enb python3
# coding=utf-8


def main():
    max_length = 0
    while True:
        word = input("Please enter a word (press ENTER on a blank line to end): ")
        word_length = len(word)
        if word_length == 0:
            break
        # if word_length > max_length:
        #     max_length = word_length
        max_length = max(word_length, max_length)
    print(f"The longest word you entered had {max_length} characters.")


if __name__ == "__main__":
    main()
