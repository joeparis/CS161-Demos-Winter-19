#!/usr/bin/env python3
import string

translator = str.maketrans("", "", string.punctuation)

# my_file = open("simple_text.txt")
# my_file.close()

with open("simple_text.txt", "r", encoding="utf-8") as text_reader:
    words = [
        word
        for line in text_reader.readlines()
        for word in line.translate(translator).split()
    ]
    words = sorted(words, key=str.lower)
    average_len = sum(len(word) for word in words) / len(words)

    print(words)
    print(f"The average word length is {average_len:.1f} characters")

