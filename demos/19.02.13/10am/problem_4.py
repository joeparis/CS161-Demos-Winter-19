#! /usr/bin/env python3

user_input = input("Please enter some words separated by commas: ")

list_of_words = [word.strip() for word in user_input.split(",")]

unique_words = []
for word in sorted(list_of_words):
    if word not in unique_words:
        unique_words.append(word)

unique_words = set(sorted(list_of_words))


print(list_of_words)
print(unique_words)
