#!/usr/bin/python3
"""
Definition of the Square class
"""


class Square:
    """
    Represents a square with a private size attribute
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a private size attribute

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size  # Utilise le setter pour validation

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #

        If size is 0, prints an empty line
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
