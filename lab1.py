############################################################
# Name: Yahia Abdelsalam
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#

from math import factorial
from functools import reduce

def inverse(x):
    """
    Returns the reciprocal of x.

    Parameters:
        x (float): The number for which the reciprocal is to be calculated.

    Returns:
        float: The reciprocal of x.
    """
    return 1.0 / x

print(inverse(4)) 
print(inverse(14)) 
print(inverse(42)) 


def e(n):
    """
    Approximates the mathematical constant 'e' using the Taylor expansion.

    Parameters:
        n (int): The number of terms to include in the expansion (1 through n).

    Returns:
        float: The approximation of e.
    """
    recips = map(lambda x: inverse(factorial(x)), range(1, n + 1))
    total = reduce(lambda a, b: a + b, recips, 0)  # Sum using reduce
    return 1 + total  # Add 1 for the first term of the Taylor expansion

print(e(2))  
print(e(3))  
print(e(10)) 
print(e(35)) 
