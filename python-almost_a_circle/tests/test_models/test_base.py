import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import os


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Resets __nb_objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for id"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base(-4)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, -4)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(4, 5)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(0, 0)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 6)
        self.assertEqual(r3.area(), 0)

    def test_perimeter(self):
        """Test perimeter method"""
        r1 = Rectangle(4, 5)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(0, 0)
        self.assertEqual(r1.perimeter(), 18)
        self.assertEqual(r2.perimeter(), 10)
        self.assertEqual(r3.perimeter(), 0)

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()),
                             [r1.to_dictionary(), r2.to_dictionary()])
        os.remove("Rectangle.json")

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(3, 5, 7, 9, 12)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 3)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertTrue(all(isinstance(i, Rectangle)
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'width')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'height')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'x')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'y')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'id')
                            for i in list_rectangles_output))

        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
