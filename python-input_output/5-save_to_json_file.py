#!/usr/bin/python3

"""
This module contains a function for saving an
object to a text file in JSON format.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
