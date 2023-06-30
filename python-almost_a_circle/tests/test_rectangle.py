import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r1 = Rectangle(10, 15, 8, 9, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 15)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.id, 1)

    def test_area(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_update(self):
        r1 = Rectangle(10, 15, 8, 9, 1)
        r1.update(width=12)
        self.assertEqual(r1.width, 12)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 15, 8, 9, 1)
        d1 = r1.to_dictionary()
        self.assertEqual(
            d1, {'id': 1, 'width': 10, 'height': 15, 'x': 8, 'y': 9})

    def test_validation_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 10)
        with self.assertRaises(ValueError):
            Rectangle(-10, 10)
        with self.assertRaises(TypeError):
            Rectangle(10, "10")
        with self.assertRaises(ValueError):
            Rectangle(10, -10)
        with self.assertRaises(TypeError):
            Rectangle(10, 10, "10")
        with self.assertRaises(ValueError):
            Rectangle(10, 10, -10)
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 10, "10")
        with self.assertRaises(ValueError):
            Rectangle(10, 10, 10, -10)

    def test_str_representation(self):
        """Test the string representation of the Rectangle"""
        r1 = Rectangle(10, 15, 8, 9, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 8/9 - 10/15")


if __name__ == "__main__":
    unittest.main()
