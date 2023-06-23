#!/usr/bin/python3

"""
This script adds all command line arguments to a Python
list and saves them to a JSON file.
"""


import sys
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

def add_items_to_json_list():
    """
    Add command line arguments to a Python list and save them to a JSON file.
    """
    # Load existing list from file, or create a new empty list
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    # Add command line arguments to the list
    existing_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(existing_list, 'add_item.json')

if __name__ == '__main__':
    add_items_to_json_list()
