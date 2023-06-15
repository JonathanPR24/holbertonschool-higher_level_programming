#!/usr/bin/python3
"""
This module have a class
that defines a rectangle
"""


def __init__(self, width=0, height=0):
    """
    Initializes a Rectangle instance.

    Args:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """
    self.width = width
    self.height = height

@property
def width(self):
    """
    Getter for the width attribute.

    Returns:
        int: The width of the rectangle.
    """
    return self.__width

@width.setter
def width(self, value):
    """
    Setter for the width attribute.

    Args:
        value (int): The width value to set.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError('width must be an integer')
    elif value < 0:
        raise ValueError('width must be >= 0')
    self.__width = value

@property
def height(self):
    """
    Getter for the height attribute.

    Returns:
        int: The height of the rectangle.
    """
    return self.__height

@height.setter
def height(self, value):
    """
    Setter for the height attribute.

    Args:
        value (int): The height value to set.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError('height must be an integer')
    elif value < 0:
        raise ValueError('height must be >= 0')
    self.__height = value

def area(self):
    """
    Calculate and return the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return self.__width * self.__height

def perimeter(self):
    """
    Calculate and return the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """
    return 2 * (self.__width + self.__height)

def __str__(self):
    """
    Return a string representation of the rectangle.

    Returns:
        str: The string representation of the rectangle.
    """
    if self.__width == 0 or self.__height == 0:
        return ""
    rectangle_str = ""
    for _ in range(self.__height):
        rectangle_str += "#" * self.__width + "\n"
    return rectangle_str[:-1]  # Remove the trailing newline character
