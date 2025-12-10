#!/usr/bin/python3
"""
Square class that defines a square with size and position properties,
area method, and my_print method with horizontal and vertical offsets.
"""


class Square:
    """Represents a square with coordinates (position)."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation (only int, reject bool, and >= 0)."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position with validation:
        must be a tuple of 2 positive integers (reject bool explicitly).
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        x, y = value
        if (type(x) is not int or type(y) is not int or x < 0 or y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = (x, y)

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #, respecting horizontal/vertical offsets."""
        if self.__size == 0:
            print()
            return

        # vertical offset: print empty lines, no spaces on those lines
        for _ in range(self.__position[1]):
            print()

        # horizontal offset + hashes on each line
        prefix = " " * self.__position[0]
        line = "#" * self.__size
        for _ in range(self.__size):
            print(prefix + line)
