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
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])
    def test_non_list(self):
        """
        Test if a TypeError is raised when the input is a string.
        """
        with self.assertRaises(TypeError):
            max_integer("string")
    def test_nested_list(self):
        """
        Test if a TypeError is raised when the list contains other lists.
        """
        with self.assertRaises(TypeError):
            max_integer([[1, 2, 3], [4, 5, 6]])
if __name__ == '__main__':
    unittest.main()
