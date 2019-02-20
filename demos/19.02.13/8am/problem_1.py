#! /usr/bin/env python3

from random import randint

# nums = [1,4,5,3,8]
nums = [randint(1, 1337) for n in range(10)]

# this is the equivalent code for the comprehension above
# nums []
# for _ in range(10):
#     nums.append(randint(1, 1337))


print(nums)
print(sum(nums))

