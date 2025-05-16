#!/usr/bin/python3
"""
Function that adds 2 integers.
a and b must be integers or floats
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """ Add to integers or floats
        a: first number
        b: second number
        Return: the result of the addition of two a and b
        Raise: TypeError if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
