#!/usr/bin/env python3
import os

print(os.environ.get("foo", "foo environment variable not found"))
print(os.environ.get("quxx", "quux environment variable not found"))
print(os.environ.get("home", "home environment variable not found"))
print(os.environ.get("HOME," "HOME environment variable not found"))
print(os.cpu_count())
print(os.getenv("foo"))
print(os.getenv("bar", default="Whoopie"))

