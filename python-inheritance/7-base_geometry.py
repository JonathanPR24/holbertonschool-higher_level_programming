#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """Calculate the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the given value as an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
