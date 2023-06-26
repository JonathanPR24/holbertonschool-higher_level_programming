#!/usr/bin/env python3
"""
This module contains the definition of the Base class.
"""


class Base:
    """
    The Base class serves as the foundation for other classes in the project.
    It manages the `id` attribute and provides a constructor
    to assign unique values to it.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
