#!/usr/bin/python3
"""
This module contains a unittest class for the function max_integer().
"""

import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A unittest class for max_integer()
    """

    def test_basic(self):
        """
        Test normal cases for the function.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertIsNone(max_integer([]))

    def test_string(self):
        """
        Test if a TypeError is raised when the list contains strings.
        """
        try:
            max_integer(['a', 'b', 'c'])
        except TypeError:
            self.assertTrue(True)
        else:
            self.assertTrue(False, "TypeError not raised")

    def test_non_list(self):
        """
        Test if a TypeError is raised when the input is a string.
        """
        try:
            max_integer("string")
        except TypeError:
            self.assertTrue(True)
        else:
            self.assertTrue(False, "TypeError not raised")

    def test_nested_list(self):
        """
        Test if a TypeError is raised when the list contains other lists.
        """
        try:
            max_integer([[1, 2, 3], [4, 5, 6]])
        except TypeError:
            self.assertTrue(True)
        else:
            self.assertTrue(False, "TypeError not raised")


if __name__ == '__main__':
    unittest.main()
