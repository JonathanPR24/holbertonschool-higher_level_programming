#!/usr/bin/python3
"""This module contains the class Student"""


class Student:
    """Declaration of class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of the Student class
        """
        if attrs is not None:
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
        else:
            return self.__dict__
