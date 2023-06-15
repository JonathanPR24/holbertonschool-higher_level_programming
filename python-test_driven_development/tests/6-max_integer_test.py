#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test max_integer with a list containing negative numbers"""
        result = max_integer([-1, -5, -3, -2])
        self.assertEqual(result, -1)

        result = max_integer([-10, -5, -8, -12, -3])
        self.assertEqual(result, -3)

    def test_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers"""
        result = max_integer([1, 2, 2, 3, 4])
        self.assertEqual(result, 4)

        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_single_element_list(self):
        """Test max_integer with a list containing a single element"""
        result = max_integer([10])
        self.assertEqual(result, 10)

        result = max_integer([-5])
        self.assertEqual(result, -5)

    def test_large_list(self):
        """Test max_integer with a large list of numbers"""
        large_list = list(range(10**6))
        result = max_integer(large_list)
        self.assertEqual(result, 999999)

    def test_float_numbers(self):
        """Test max_integer with a list containing float numbers"""
        result = max_integer([1.5, 2.3, 3.7, 4.2])
        self.assertEqual(result, 4.2)

        result = max_integer([5.9, 5.5, 5.1, 5.7])
        self.assertEqual(result, 5.9)

    def test_mixed_data_types(self):
        """Test max_integer with a list containing mixed data types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

        with self.assertRaises(TypeError):
            max_integer([True, False, True, True])

if __name__ == '__main__':
    unittest.main()
