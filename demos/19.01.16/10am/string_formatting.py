#! /user/bin/python3
# coding=utf-8

"""
Demonstrate various methods of formatting text output in Python.
"""

name = "Susan"
count = 37
PI = 3.1415

### old-school way ###
# You should not be using this type of output formatting in new Python code
# that you are writing today but you may encounter it if you search for help or
# if you inherit older code.
# print("Hello, %s. How are you today?" % (name))
# print("Hello, %s. How are you today? You have %s coconuts." % (name, count))
# print("Hello, %s. How are you today? You have %4d coconuts." % (name, count))
# print("Hello, %s. How are you today? You have %4d coconuts. The value of PI is %.2f" % (name, count, PI))
# print("Hello, %s. How are you today? You have %4d coconuts. The value of PI is %6.2f" % (name, count, PI))
# print("Hello, %10s. How are you today? You have %4d coconuts. The value of PI is %6.2f" % (name, count, PI))


### the newer way of formatting output ###
# This is a fine method to use for Python 3+
# print("Hello, {}. How are you today?".format(name))
# print("Hello, {}. How are you today? You have {} coconuts.".format(name, count))
# print("Hello, {1}. How are you today? You have {1} coconuts.".format(name, count))
# print("Hello, {1}. How are you today? You have {0} coconuts.".format(name, count))
# print("Hello, {2}. How are you today? You have {2} coconuts. The value of PI is {1}".format(name, count, PI))
# print("Hello, {}. How are you today? You have {:4} coconuts.".format(name, count))
# print("Hello, {0:.3}. How are you today? You have {0:4} coconuts.".format(name, count))
# print("Hello, {0} How are you today? You have {1:4} coconuts. The value of PI is {2:6.3}".format(name, count, PI))


### the newer way of formatting output ###
# This method of string formatting was introduced in Python 3.6
# "formatted-string" or an f-string"
print(f"Hello, {name}. How are you today?")
print(f"Hello, {name}. How are you today? You have {count} coconuts.")
print(f"Hello, {name}. How are you today? You have {name} coconuts.")
print(f"Hello, {count}. How are you today? You have {name} coconuts.")
print(f"Hello, {name}. How are you today? You have {count:4} coconuts.")
print(f"Hello, {name:.3}. How are you today? You have {count:4} coconuts.".format(name, count))
print(f"Hello, {name} How are you today? You have {count:4} coconuts. The value of PI is {PI:6.3}".format(name, count, PI))


### string concatenation ###
# is BAD
print(name + " " + str(count))
print("Hello there", name, "you have", count, "coconuts.")


