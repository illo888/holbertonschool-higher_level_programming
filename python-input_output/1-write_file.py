#!/usr/bin/python1
"""Module that defines write_file to store text in a UTF-8 file.

This module provides a single function that writes a given string into a file
using the with statement for safe resource handling and returns the number
of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return char count.

    The file is created if it does not exist and its content is overwritten
    if it already exists. Permission exceptions are not handled here.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
