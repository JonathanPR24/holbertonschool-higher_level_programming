#!/usr/bin/python3
import unittest
from max_integer import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([10, 2, 8, 4, 6]), 10)
        self.assertEqual(max_integer([1, 2, 3, 9, 7]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-10, -2, -8, -4, -6]), -2)
        self.assertEqual(max_integer([-1, -2, -3, -9, -7]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([10, -2, 8, -4, 6]), 10)
        self.assertEqual(max_integer([-1, 2, -3, 9, -7]), 9)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-3, -3, -3, -3]), -3)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
