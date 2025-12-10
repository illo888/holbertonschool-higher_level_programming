
#!/usr/bin/python3
"""
Square class that defines a square with private size,
a size property with validation, and an area method.
"""


class Square:
    """Represents a square with a private size and controlled access."""

    def __init__(self, size=0):
        """Initialize Square with optional size (default: 0)."""
        self.size = size  # use the property to apply validation

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation (reject bool, allow only ints >= 0)."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
