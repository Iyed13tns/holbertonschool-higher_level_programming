import unittest

#!/usr/bin/python3
"""
Unittest for add_integer function
"""
from 0-add_integer import add_integer

class TestAddInteger(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add_integer(1, 2), 3)

    def test_add_integer_and_float(self):
        self.assertEqual(add_integer(100, 2.5), 102)

    def test_default_b(self):
        self.assertEqual(add_integer(2), 100)

    def test_negative_numbers(self):
        self.assertEqual(add_integer(-1, -2), -3)

    def test_large_numbers(self):
        self.assertEqual(add_integer(1000000000, 2000000000), 3000000000)

    def test_invalid_a(self):
        with self.assertRaises(TypeError):
            add_integer("string", 2)

    def test_invalid_b(self):
        with self.assertRaises(TypeError):
            add_integer(2, "string")

    def test_none_a(self):
        with self.assertRaises(TypeError):
            add_integer(None, 2)

    def test_none_b(self):
        with self.assertRaises(TypeError):
            add_integer(2, None)

if __name__ == '__main__':
    unittest.main()