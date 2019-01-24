"""
A simple program to calculate a chaotic function.

This program will calculate the first ten values of a chaotic
function with the form k(x)(1-x) where k=3.9 and x is provided
by the user.
"""

def main():
    """
    Calculate the values of the chaotic function.
    """
    x = float(input("Enter a number between 1 and 0: "))
    # We will avoid using eval() because it is a security concern.
    # x = eval(input("Enter a number between 1 and 0: "))
    for _ in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
    
  
# identifiers that start and end with double underscores (sometimes called
# "dunders") are special in Python. 
if __name__ == "__main__":
    main()

    