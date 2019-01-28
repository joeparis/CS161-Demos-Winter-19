#! /usr/bin/env python3
# coding =utf-8

name = "Joseph"

VOWELS = "aeiou"
syllable = "ish"
index = 0

for char in name:
    if char in VOWELS:
        index = name.find(char, index)
        name = name[:index] + syllable + name[index:]
        index += len(syllable)

print(name)
