#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, None)

    def test_all_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_all_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_duplicate_numbers(self):
        result = max_integer([3, 3, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.7, 0.5, 3.0])
        self.assertEqual(result, 3.0)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3, 4])

if __name__ == '__main__':
    unittest.main()
