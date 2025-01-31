#!/usr/bin/python3
"""
Definition of the Rectangle class
"""


class Rectangle:
    """
    Represents a Rectangle with a private size attribute
    """

    def __init__(self, size):
        """
        Initializes a Rectangle instance with a private size attribute

        Args:
            size: The size of the Rectangle
        """
        self.__size = size