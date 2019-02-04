#! /usr/bin/env python3
# coding=utf-8

"""
Write a Python program that prints a table of n, n^2, and n^3 in right-aligned
columns for 1 >= n <= 10.</p>
"""


def main():
    for n in range(1, 11):
        print(f"{n:2} {n**2:3} {n**3:4}")


if __name__ == "__main__":
    main()
