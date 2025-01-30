#!/usr/bin/python3
"""
Definition of the Square class
"""


class Square:
    """
    Represents a square with size and position attributes
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square
            position (tuple): The position offset (x, y)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
            TypeError: If position is not a tuple of 2 positive integers
        """
        self.size = size  # Utilise le setter pour valider
        self.position = position  # Utilise le setter pour valider

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation"""
        if (
            not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        # Gère les sauts de ligne en fonction de position[1]
        print("\n" * self.__position[1], end="")

        # Affiche le carré avec les espaces de position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
