"""
This program computes the first ten values of a chaotic function.

This program will compute the first ten values of a chaotic function with
the form x=k(x)(1-x) where k=3.9 and x is provided by the user.
"""

def calc():
    """
    This function is where the values of the chaotic function are computed.
    """
    x = float(input("Please enter a number between 0 and 1: "))
    # eval has secutiry implications, NEVER accept run un-sanitized input
    # from the user
    # x = eval(input("Please enter a number between 0 and 1: "))
    for _ in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
    
    
if __name__ = '__main__':
    calc()