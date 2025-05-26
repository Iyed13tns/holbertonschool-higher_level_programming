#!/usr/bin/python3

"""
Function that returns the list
of available attributes and methods.
"""


def lookup(obj):
    """
    This function returns the list of attributes and methods of an object.
    """
    return dir(obj)
