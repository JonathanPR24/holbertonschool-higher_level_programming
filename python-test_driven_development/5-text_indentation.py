#!/usr/bin/python3
"""
This module contains a function that indents text
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text: The text to print. Must be a string.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, "{}\n\n".format(char))

    print("\n".join(line.strip() for line in text.split("\n")))
