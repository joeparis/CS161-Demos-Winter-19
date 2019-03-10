#!/usr/bin/env python3

with open("long_int.txt", "r") as int_reader:
    nums = sorted([int(num) for num in int_reader.readlines()], reverse=True)

    for num in nums:
        print(f"{num:,}")
