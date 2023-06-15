#!/usr/bin/python3
"""
This module contains a function that indents text
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    indented_lines = []
    current_line = ""

    for char in text:
        current_line += char

        if char in punctuation_marks:
            indented_lines.append(current_line.strip())
            indented_lines.append("")
            current_line = ""

    if current_line:
        indented_lines.append(current_line.strip())

    print("\n".join(indented_lines))
