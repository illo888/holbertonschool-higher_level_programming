#!/usr/bin/python3
"""
0-add_integer Module
This module contains one function: add_integer(a, b=98).
The function adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number, defaults to 98.

    Returns:
        int: The sum of a and b after casting to integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
