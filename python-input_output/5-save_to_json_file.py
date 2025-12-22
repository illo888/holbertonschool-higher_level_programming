#!/usr/bin/python3
"""Module that defines save_to_json_file to store objects as JSON.

This module provides a function that writes a Python object to a text file
using its JSON representation with the standard json library.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation.

    Args:
        my_obj: Any Python object that can be serialized by json.
        filename (str): Path to the destination file.

    Note:
        Exceptions for non-serializable objects or permissions are not handled
        here, as per the task requirements.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
