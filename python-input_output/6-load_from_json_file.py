#!/usr/bin/python3

"""
This module contains a function for loading an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
