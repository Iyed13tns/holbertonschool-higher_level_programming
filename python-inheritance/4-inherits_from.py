#!/usr/bin/python3
'''
j
'''


def inherits_from(obj, a_class):
    """
    u
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
