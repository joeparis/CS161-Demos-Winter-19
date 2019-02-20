#! /usr/bin/env python3
import random
import string

# letters = ["a", "b", "c", "d", "e"]

my_string = "".join(random.choice(string.ascii_letters) for _ in range(15))

print(my_string)
print(type(my_string))
