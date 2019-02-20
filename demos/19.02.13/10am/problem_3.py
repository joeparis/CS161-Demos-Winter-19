#! /usr/bin/env python3
import random

nums = [random.randint(1, 37) for n in range(12) if n % 2 != 0]

# this is the equivalent version of the comprehension above
num = []
for n in range(12):
    x = random.randint(1, 37)
    if x % 2 != 0:
        nums.append(x)

## Joe's solution
# print(nums)
# print(max(nums))

## Sam's solution
# biggest = 0
# for num in nums:
#     if num > biggest:
#         biggest = num
# print(biggest)

## 8am class' solution(s)
# list.sort() sorts *in place*
# nums.sort()
# print(nums)
# print(nums[-1])
# sorted() returns a *new* list of elements
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)
# print(sorted_nums[0])

