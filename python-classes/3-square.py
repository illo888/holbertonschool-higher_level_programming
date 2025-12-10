#!/usr/bin/python3
"""
Square class that defines a square with private size and area method.
"""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size=0):
        """Initialize Square with optional size (default: 0)."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
