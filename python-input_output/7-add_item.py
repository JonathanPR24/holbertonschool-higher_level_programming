#!/usr/bin/python3
"""
This module contains a script that
adds all arguments to a Python list
and saves them to a file.
"""


import sys
import json
from typing import List


def save_to_json_file(my_obj: List[str], filename: str) -> None:
    """Save a list object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename: str) -> List[str]:
    """Load a list object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def add_items_to_json_list():
    """Add command line arguments to a Python list and
    save them to a JSON file."""
    filename = "add_item.json"
    js_list = load_from_json_file(filename) if filename in sys.argv[1:] else []

    js_list.extend(sys.argv[1:])
    save_to_json_file(js_list, filename)


if __name__ == "__main__":
    add_items_to_json_list()
