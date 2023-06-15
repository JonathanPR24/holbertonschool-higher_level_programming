import unittest
from max_integer import max_integer


class MaxIntegerTestCase(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: Regular list
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: List with unordered elements
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test case 3: List with negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: List with duplicate maximum values
        self.assertEqual(max_integer([1, 2, 4, 4]), 4)

        # Test case 5: Empty list
        self.assertIsNone(max_integer([]))

        # Test case 6: List with a single element
        self.assertEqual(max_integer([5]), 5)


if __name__ == '__main__':
    unittest.main()
