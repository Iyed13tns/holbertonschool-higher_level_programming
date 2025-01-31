#!/usr/bin/python3
"""
Definition of the Rectangle class
"""


class Rectangle:

    def __init__(self, width, height):
        
        
        self.__width = width
        self.__height = height


    @property
    def width(self, value):
        return self.__width
