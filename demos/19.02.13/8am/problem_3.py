#! /usr/bin/env python3
from random import randint

nums = [randint(1, 37) for _ in range(15)]

# largest_num = max(nums)
# print(largest_num)

nums.sort()
print(nums)
print(nums[-1])

sorted_nums = sorted(nums, reverse=True)
print(sorted_nums)
print(sorted_nums[0])

# my_string = "big bird"
# print("".join(sorted(my_string)))

