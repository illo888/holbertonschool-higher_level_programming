#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev = 0
    for ch in roman_string.upper():
        val = values.get(ch, 0)
        if val == 0:
            return 0
        if val > prev:
            total += val - 2 * prev
        else:
            total += val
        prev = val
    return total
