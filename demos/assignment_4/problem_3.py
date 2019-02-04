#! /usr/bin/env python3
# coding=utf-8

"""
Write a Python program that accepts an integer n and computes the value of
n+nn+nnn.

For example, if n=5 then compute 5 + 55 + 555 = 615</p>
"""


def method_1(n):
    value_1 = int(f"{n}")
    value_2 = int(f"{n}{n}")
    value_3 = int(f"{n}{n}{n}")
    print(f"{value_1} + {value_2} + {value_3} = {value_1 + value_2 + value_3}")


def method_2(n):
    nums = []
    for i in range(1, 4):
        num = n * i
        nums.append(int(num))
    print(f"{nums[0]} + {nums[1]} + {nums[2]} = {sum(nums)}")


def method_3(n):
    print(sum([int(n * idx) for idx in range(1, 4)]))


if __name__ == "__main__":
    # n = input("Please enter a value, x, and I will computer x + xx + xxx: ")
    n = "5"
    method_1(n)
    method_2(n)
    method_3(n)
