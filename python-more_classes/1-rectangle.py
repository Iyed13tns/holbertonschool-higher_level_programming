#!/usr/bin/python3
"""
Module contenant la définition de la classe Rectangle.
"""


class Rectangle:
    """
    Classe représentant un rectangle.

    Attributes:
        __width (int): Largeur du rectangle (privée).
        __height (int): Hauteur du rectangle (privée).
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur données.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter pour la largeur du rectangle.

        Returns:
            int: La largeur du rectangle.
        """
        return self.__width
