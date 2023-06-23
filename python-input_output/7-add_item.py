#!/usr/bin/python3
"""
This script adds all arguments to a Python list
and saves them to a file.
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.
    Args:
        my_obj: The object to be saved.
        filename: The name of the file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.
    Args:
        filename: The name of the file.
    Returns:
        The loaded object.
    """
    with open(filename, 'r') as file:
        return json.load(file)


def add_items_to_list_and_save(filename, *args):
    """
    Add command line arguments to a Python list and save them to a JSON file.
    Args:
        filename: The name of the file.
        args: The command line arguments to be added to the list.
    """
    try:
        items_list = load_from_json_file(filename)
    except FileNotFoundError:
        items_list = []

    items_list.extend(args)
    save_to_json_file(items_list, filename)


if __name__ == "__main__":
    add_items_to_list_and_save("add_item.json", *sys.argv[1:])
