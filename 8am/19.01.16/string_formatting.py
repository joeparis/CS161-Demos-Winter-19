#! /usr/bin/python3
# coding=utf-8

"""
A quick and dirty review of Python print() formatting.
"""


name = "Joe"
answer = 42
PI = 3.14

### "old-school method" ###
# print("Hello %s" % name)
# print("Hello %s %s" % (name, answer))
# print("Hello %s %d" % (name, answer))
# print("Hello %s %4d" % (name, answer))
# print("Hello %s %4d %f" % (name, answer, PI))
# print("Hello %s %4d %.2f" % (name, answer, PI))
# print("Hello %s %4d %6.3f" % (name, answer, PI))

### .format() example ###
# print("Hello {}".format(name))
# print("Hello {}, the answer is {}".format(name, answer))
# print("Hello {1}, the answer is {0}".format(name, answer))
# print("Hello {1}, the answer is {1}".format(name, answer))
# print("Hello {}, the answer is {:6}".format(name, answer))
# print("Hello {1:6}, the answer is {0}".format(name, answer))
# print("Hello {:10}, the answer is {:6}, PI is {:6.2}".format(name, answer, PI))

### f-strings ###
print(f"Hello {name}")
print(f"Hello {name}, the answer is {answer}")
print(f"Hello {answer}, the answer is {name}")
print(f"Hello {name}, the answer is {answer}")
print(f"Hello {name}, the answer is {answer:6}")
print(f"Hello {name:6}, the answer is {answer}")
print(f"Hello {name:10}, the answer is {answer:6}, PI is {PI:6.2}")
