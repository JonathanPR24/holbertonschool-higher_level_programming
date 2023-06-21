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
