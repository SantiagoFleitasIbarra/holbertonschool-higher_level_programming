#!/usr/bin/python3
"""Unittest for Rectangle()"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """this define a class test"""
    def test_constructor(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("5", 10)
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "10")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "2")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -2)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 2, "3")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 2, -3)

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_str(self):
        rect = Rectangle(4, 5, 2, 1, 8)
        self.assertEqual(str(rect), "[Rectangle] (8) 2/1 - 4/5")

    def test_update(self):
        rect = Rectangle(4, 5, 2, 1, 8)
        rect.update(9, 3, 2, 0, 4)
        self.assertEqual(rect.id, 9)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        rect = Rectangle(4, 5, 2, 1, 8)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'id': 8, 'width': 4, 'height': 5, 'x': 2, 'y': 1})

if __name__ == '__main__':
    unittest.main()
