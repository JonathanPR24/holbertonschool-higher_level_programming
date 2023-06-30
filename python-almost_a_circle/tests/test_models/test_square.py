import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_attributes(self):
        s1 = Square(5, 1, 2, 3)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 3)

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_update(self):
        s1 = Square(5)
        s1.update(size=7)
        self.assertEqual(s1.size, 7)

    def test_to_dictionary(self):
        s1 = Square(5, 1, 2, 3)
        d1 = s1.to_dictionary()
        self.assertEqual(d1, {'id': 3, 'size': 5, 'x': 1, 'y': 2})

    def test_validation_errors(self):
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(ValueError):
            Square(-10)
        with self.assertRaises(TypeError):
            Square(10, "10")
        with self.assertRaises(ValueError):
            Square(10, -10)
        with self.assertRaises(TypeError):
            Square(10, 10, "10")
        with self.assertRaises(ValueError):
            Square(10, 10, -10)

    def test_str_representation(self):
        """Test the string representation of the Square"""
        s1 = Square(5, 1, 2, 3)
        self.assertEqual(str(s1), "[Square] (3) 1/2 - 5")


if __name__ == "__main__":
    unittest.main()
