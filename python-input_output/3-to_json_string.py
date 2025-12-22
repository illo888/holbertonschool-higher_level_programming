#!/usr/bin/python3
"""Module that defines to_json_string for JSON serialization.

This module provides a function that returns the JSON string representation
of a given Python object using the standard json library.
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation (str) of a Python object.

    Args:
        my_obj: Any Python object that can be serialized by json.

    Returns:
        str: JSON string representation of the input object.

    Note:
        Exceptions for non-serializable objects are not handled here,
        as per the task requirements.
    """
    return json.dumps(my_obj)
