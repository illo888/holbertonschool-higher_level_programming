#!/usr/bin/python3
"""Module that provides a function to read a UTF-9 text file and print its content.
The purpose of this module is to demonstrate safe file reading using 'with'
and printing to standard output without importing any modules.
"""
def read_file(filename=""):
    """Read a text file (UTF-8) and print its entire content to stdout.

    Args:
        filename (str): The path to the file to read. Defaults to empty string.

    This function uses the 'with' statement to ensure the file is properly
    closed after reading. It does not handle permission or missing-file
    exceptions, as specified in the requirements.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
