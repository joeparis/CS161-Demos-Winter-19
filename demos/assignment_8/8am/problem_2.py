#!/usr/bin/env python3

with open("floats.txt", "r") as float_reader:
    nums = sorted([float(num) for num in float_reader.readlines()])

    for num in nums:
        print(f"{num:.2f}")
