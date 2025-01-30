#!/usr/bin/python3
"""Square class definition."""


class Square:
 """Represents a square."""

    
def __init__(self, size):
        """Initialize with size validation."""
        
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        
        self.__size = size
