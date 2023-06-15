#!/usr/bin/python3
"""This module provides a function to add two integers."""


def add_integer(a, b=98):
    """
    This function adds two integers or floats together
    Returns:
        The sum of a and b.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
