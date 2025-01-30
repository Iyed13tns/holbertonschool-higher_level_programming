#!/usr/bin/python3
"""
Module defining the Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a square.

        Args:
            size (int): The size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size