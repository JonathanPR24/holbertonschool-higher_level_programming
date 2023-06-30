import unittest
import io
import unittest.mock

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    """ Testing width conditions """
    def test_width(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.width, 2)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-4, 1)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 5)

    def test_string_width(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("2", 10)

    """ Testing height conditions """
    def test_height(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.height, 4)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, -2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 0)

    def test_str_height(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(35, "15")

    """ Testing x conditions """
    def test_x(self):
        rectangle = Rectangle(10, 2, 3, 5)
        self.assertEqual(rectangle.x, 3)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 5, -9)

    def test_x_zero(self):
        rectangle = Rectangle(3, 2, 0, 1)
        self.assertEqual(rectangle.x, 0)

    def test_x_str(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 5, "1")

    """ Testing y conditions """
    def test_y(self):
        rectangle = Rectangle(2, 3, 2, 2)
        self.assertEqual(rectangle.y, 2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 2, 3, -1)

    def test_y_zero(self):
        rectangle = Rectangle(3, 2, 1, 0)
        self.assertEqual(rectangle.y, 0)

    def test_y_str(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(4, 6, 2, "2")

    """ Testing area """
    def test_area(self):
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.area(), 9)

    def test_area_2(self):
        rectangle = Rectangle(2, 10)
        self.assertEqual(rectangle.area(), 20)

    def test_area_3(self):
        rectangle = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rectangle.area(), 56)

    """ Testing display """
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        rectangle = Rectangle(2, 2, 1, 1)
        rectangle.display()
        self.assertEqual(mock_stdout.getvalue(), "##\n##\n")

        rectangle = Rectangle(2, 3, 2, 2)
        rectangle.display()
        self.assertEqual(mock_stdout.getvalue(), "##\n##\n##\n")

        rectangle = Rectangle(3, 2, 1, 0)
        rectangle.display()
        self.assertEqual(mock_stdout.getvalue(), "###\n###\n")

    @unittest.expectedFailure
    def test_display_failure(self):
        rectangle = Rectangle(0, 0, 0, 0)
        rectangle.display()

    """ Testing __str__ """
    def test_str_method(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    """ Testing update method """
    def test_update(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89)
        self.assertEqual(rectangle.id, 89)
        rectangle.update(89, 2)
        self.assertEqual(rectangle.width, 2)
        rectangle.update(89, 2, 3)
        self.assertEqual(rectangle.height, 3)
        rectangle.update(89, 2, 3, 4)
        self.assertEqual(rectangle.x, 4)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(rectangle.y, 5)

    """  Testing to_dictionary method """
    def test_to_dictionary(self):
        rectangle = Rectangle(10, 2, 1, 9, 7)
        expected_dict = {'x': 1, 'y': 9, 'id': 7, 'height': 2, 'width': 10}
        self.assertDictEqual(rectangle.to_dictionary(), expected_dict)

    """ Testing create method """
    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    """ Testing save to file """
    def test_save_to_file_empty(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file_empty_2(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        expected_output = '[{"x": 0, "y": 0, "id": 18, "height": 2, "width": 1}]'
        with open("Rectangle.json") as fd:
            self.assertEqual(expected_output, fd.read())

    """ Testing load from file """
    def test_load(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertNotEqual(loaded_rectangles[0], r1)


if __name__ == '__main__':
    unittest.main()
