#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation
of an object (string).
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
