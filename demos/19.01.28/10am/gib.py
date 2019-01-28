#! /usr/bin/env python3
# coding =utf-8

VOWELS = "aeiou"  # strings are iterable
name = "bookkeeper"
syllable = "ooh"
index = 0

for character in name:
    if character.lower() in VOWELS:
        index = name.find(character, index)
        name = name[:index] + syllable + name[index:]
        index += len(syllable) + 1

print(name)

