#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description with simple data structure for JSON serialization
of an object.
"""


class MyClass:
    """
    My class.
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj (object): An instance of a Class.

    Returns:
        dict: A dictionary representing the object's attributes.

    """
    attributes = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[attr] = value
    return attributes
