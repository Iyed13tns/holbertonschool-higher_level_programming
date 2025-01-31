#!/usr/bin/python3
"""
Definition of the Rectangle class
"""


class Rectangle:
    """
    Represents a Rectangle with private width and height attributes.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with private width and height attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
