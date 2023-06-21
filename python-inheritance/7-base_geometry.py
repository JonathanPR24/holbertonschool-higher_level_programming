#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


class BaseGeometry:
    """
    Base class representing geometry.

    This class serves as a base class that can be inherited by other classes
    to provide common geometry functionality.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the `area()` method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
