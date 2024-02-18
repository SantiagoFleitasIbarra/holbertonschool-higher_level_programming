#!/usr/bin/python3
"""Unittest for Base()"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """this define a class test"""
    def test_init(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

        obj2 = Base(5)
        self.assertEqual(obj2.id, 5)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'key': 'value'}]), '[{"key": "value"}]')

    def test_save_to_file(self):
        class DummyObj:
            def to_dictionary(self):
                return {'key': 'value'}

        obj_list = [DummyObj()]

        Base.save_to_file(obj_list)

        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), '[{"key": "value"}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"key": "value"}]'), [{'key': 'value'}])

if __name__ == '__main__':
    unittest.main()
