#!/usr/bin/python3
"""
This module contains the Base class.
"""


import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base instance.

        Args:
            id (int, optional): ID to assign to the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs] 
        if list_objs is not None else []
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Load a list of objects from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + '.json'
        if not filename:
            return []
        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**dictionary) for dictionary in list_dicts]

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes already set based on a dictionary.

        Args:
            **dictionary: Dictionary containing attribute-value pairs.

        Returns:
            obj: Instance with attributes set.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
