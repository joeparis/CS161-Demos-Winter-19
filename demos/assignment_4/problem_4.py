#! /usr/bin/env python3
# coding=utf-8

"""
Write a Python program to create a Caesar encryption.

In cryptography, a Caesar cipher is one of the simplest and most widely
known encryption techniques. It is a type of substitution cipher in which
each letter in the plaintext is replaced by a letter some fixed number of
positions down the alphabet. For example, with a left shift of 3, D would be
replaced by A, E would become B, and so on. The method is named after Julius
Caesar, who used it in his private correspondence.
"""


def good(plain_text, key):
    for character in plain_text:
        print(f"{character} --> {chr(ord(character) + key)}")


def better(plain_text, key):
    scratch = []

    for character in plain_text:
        if character.isalpha():
            new_character = ord(character) + key
            if character.islower():
                if new_character > ord("z"):
                    new_character -= 26
                elif new_character < ord("a"):
                    new_character += 26
            elif character.isupper():
                if new_character > ord("Z"):
                    new_character -= 26
                elif new_character < ord("A"):
                    new_character += 26
            scratch.append(chr(new_character))
        else:
            scratch.append(character)
    encrypted_text = "".join(scratch)
    print(encrypted_text)


def best(plain_text, key):
    pass


if __name__ == "__main__":
    plain_text = input("Enter the phrase to be encoded: ")
    key = int(input("Enter the key value: "))
    # good(plain_text, key)
    better(plain_text, key)
    # best(plain_text, key)
