#!/usr/bin/python3
"""Unittest for Square()"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            square = Square("5")
        with self.assertRaises(ValueError):
            square = Square(-5)

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_str(self):
        square = Square(4, 2, 1, 8)
        self.assertEqual(str(square), "[Square] (8) 2/1 - 4")

    def test_update(self):
        square = Square(4, 2, 1, 8)
        square.update(9, 3, 0, 4)
        self.assertEqual(square.id, 9)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        square = Square(4, 2, 1, 8)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 8, 'size': 4, 'x': 2, 'y': 1})

if __name__ == '__main__':
    unittest.main()
