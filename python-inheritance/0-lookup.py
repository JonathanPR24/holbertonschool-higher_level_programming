#!/usr/bin/python3
""" Module to lookup attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to look up attributes and methods for.

    Returns:
        A list containing the attributes and methods of the object.
    """
    return dir(obj)
