#!/usr/bin/python3
"""
This module contains a function for writing a string to a
text file and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to write to. (default "")
        text (str): The string to write to the file. (default "")

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
