#! /usr/bin/env python3
# coding=utf-8


def method_1(n):
    print(n * 1 + n * 11 + n * 111)


def method_2(n):
    value_1 = int(f"{n}")
    value_2 = int(f"{n}{n}")
    value_3 = int(f"{n}{n}{n}")
    print(f"{value_1} + {value_2} + {value_3} = {value_1 + value_2 + value_3}")


def method_3(n):
    nums = []
    for i in range(1, 4):
        num = n * i
        nums.append(int(num))
    print(f"{nums[0]} + {nums[1]} + {nums[2]} = {sum(nums)}")


def method_4(n):
    print(sum([int(n * i) for i in range(1, 4)]))


if __name__ == "__main__":
    n = input("Please enter a number 0 <= n < 10:  ")
    # method_1(n)
    # method_2(n)
    # method_3(n)
    method_4(n)
