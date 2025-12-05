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
        TypeError: If a or b is not an integer or float,
                   or if a or b is a NaN/Infinity float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # التعامل مع حالات Inf/NaN (تجنب استخدام math)
    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        # NaN is the only value not equal to itself (a != a)
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
