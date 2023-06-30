import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """ Testing initialization """
    def test_init(self):
        base_obj = Base()
        self.assertEqual(base_obj._Base__nb_objects, 1)
        self.assertEqual(base_obj.id, 1)

        base_obj_2 = Base()
        self.assertEqual(base_obj_2._Base__nb_objects, 2)
        self.assertEqual(base_obj_2.id, 2)

        base_obj_3 = Base(89)
        self.assertEqual(base_obj_3._Base__nb_objects, 2)
        self.assertEqual(base_obj_3.id, 89)

    """ Testing conversion to JSON string """
    def test_to_json_string(self):
        rectangle = Rectangle(10, 7, 2, 8, 1)
        rect_dict = rectangle.to_dictionary()
        json_str = Base.to_json_string([rect_dict])
        expected_json_str = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_str, expected_json_str)

    def test_to_json_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, '[]')

    def test_to_json_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')

    """ Testing conversion from JSON string """
    def test_from_json_string(self):
        json_str = Base.from_json_string(None)
        self.assertEqual(json_str, [])

    def test_from_json_str(self):
        json_str = Base.from_json_string("[]")
        self.assertEqual(json_str, [])

    def test_from_json_str_good(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_input = Base.to_json_string(list_input)
        json_output = Base.from_json_string(json_input)
        self.assertIsInstance(json_output, list)

    def test_from_json_str_empty(self):
        json_str = Base.from_json_string(None)
        self.assertEqual(json_str, [])

    def test_from_json_str_empty_2(self):
        json_str = Base.from_json_string("[]")
        self.assertEqual(json_str, [])

if __name__ == '__main__':
    unittest.main()
