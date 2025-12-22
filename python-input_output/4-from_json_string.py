#!/usr/bin/python3
"""Module that defines from_json_string to parse JSON strings.

This module provides a function that returns a Python data structure
represented by a given JSON string using the standard json library.
"""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        Any: Python data structure obtained from the JSON string.

    Note:
        Exceptions for invalid JSON input are not handled here, per
        the task requirements.
    """
    return json.loads(my_str)
