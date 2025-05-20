#!/usr/bin/python3
"""Defines a class Square that represents a square with position."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be int")
        if value < 0:
            raise ValueError("size should be >= 0")
        self.size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if type(value) != list or len(value) != 2:
            raise TypeError("position must be a list of 2 values")
        self.position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size * self.size

    def my_print(self):
        """
        Prints the square with the character '#'.

        If size is 0, prints an empty line.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print(" ")
            for i in range(self.size):
                print(" " * self.position[1] + "#" * self.size)
