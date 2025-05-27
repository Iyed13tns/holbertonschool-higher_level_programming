#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
