#!/usr/bin/python3
"""Module that checks if an object is exactly
an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class
