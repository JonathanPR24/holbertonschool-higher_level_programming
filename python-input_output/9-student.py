#!/usr/bin/python3
"""
This module contains a class Student that defines a student.
"""


class Student:
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        attributes = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                attributes[attr] = value
        return attributes
