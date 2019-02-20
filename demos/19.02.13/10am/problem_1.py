#! /usr/bin/env python3
import random


# nums = [2, 37, 42, 15]
nums = [random.randint(1, 1337) for _ in range(10)]

# unrolling the comprehension
# nums = []
# for x in range(10):
#     nums.append(random.randint(1, 1337))


print(sum(nums))

