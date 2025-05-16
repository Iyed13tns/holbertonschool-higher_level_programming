#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function ensures that inputs are integers or floats,
and raises a TypeError if they are not.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats as integers.

    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
