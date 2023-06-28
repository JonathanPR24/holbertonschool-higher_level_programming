#!/usr/bin/python3
"""
This module contains the Base class.
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base instance

        Args:
            id (int, optional): id to assign to the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
