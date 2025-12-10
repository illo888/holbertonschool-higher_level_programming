#!/usr/bin/python3
"""
Square class that defines a square with private size,
a size property with validation, and an area method.
"""


class Square:
    """Represents a square with a private size and controlled access."""

    def __init__(self, size=0):
        """Initialize Square with optional size (default: 0)."""
        # Use the property to apply validation logic centrally
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation (only int, no bool, and >= 0)."""
        # Reject bool explicitly (since bool is a subclass of int)
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
