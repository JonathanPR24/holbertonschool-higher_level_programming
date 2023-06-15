#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 12, 3]), 12)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test max_integer with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -12, -3]), -3)

    def test_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers"""
        self.assertEqual(max_integer([1, 2, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()
