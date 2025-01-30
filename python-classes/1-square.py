#!/usr/bin/python3
"""
Definition of the Square class
"""


class Square:
    """
    Represents a square with a private size attribute
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a private size attribute

        Args:
            size: The size of the square
        """
        self.__size = size
        