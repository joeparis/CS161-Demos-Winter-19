#! /usr/bin/env python3
import random
import string

# letters = ["a", "b", "c", "d"]
letters = [random.choice(string.ascii_letters) for _ in range(20)]

letters = []
for _ in range(20):
    letters.append(random.choice(string.ascii_letters))

my_string = "".join(letters)
print(letters)
print(my_string)
# long = ""

# for x in letters:
#     long += x

