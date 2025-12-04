#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Safe delete: if key exists, remove it; otherwise leave dictionary unchanged
    a_dictionary.pop(key, None)
    return a_dictionary
