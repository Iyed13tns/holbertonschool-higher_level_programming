#!/usr/bin/python3
"""
This module contains a function that writes an Object to a text file,
using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file to save the object to.
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
