#! /usr/bin/env python3
# coding=utf-8


def main(max=10):
    for n in range(1, max + 1):
        print(f"{n:8,}  {n**2:8,}  {n**3:8,}")


if __name__ == "__main__":
    main(40)
