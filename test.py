import unittest

from fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):

    def test_result_type(self):
        self.assertIsInstance(fizzbuzz(1), str) 

    def test_result_type_fizz(self):
        self.assertIsInstance(fizzbuzz(3), str) 

    def test_result_type_buzz(self):
        self.assertIsInstance(fizzbuzz(5), str) 

    def test_result_type_fizzbuzz(self):
        self.assertIsInstance(fizzbuzz(15), str) 

    def test_check_fizz(self):
        self.assertEqual(fizzbuzz(12), "fizz")

    def test_check_buzz(self):
        self.assertEqual(fizzbuzz(40), "buzz")

    def test_check_fizzbuzz(self):
        self.assertEqual(fizzbuzz(150), "fizzbuzz")

    def test_check_no_fizzbuzz(self):
        self.assertEqual(fizzbuzz(151), "151")
