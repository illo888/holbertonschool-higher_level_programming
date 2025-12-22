#!/usr/bin/python3
"""Module that defines load_from_json_file to read objects from JSON files.

This module provides a function that opens a file, reads its JSON content,
and returns the corresponding Python data structure using the standard json
library.
"""

import json


def load_from_json_file(filename):
    """Create and return a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file to read.

    Returns:
        Any: Python data structure represented by the file's JSON content.

    Note:
        Exceptions for invalid JSON content, missing files, or permissions
        are not handled here, per the task requirements.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
