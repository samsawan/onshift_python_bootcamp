# Good tutorial on unittest: https://confluence.jetbrains.com/display/PYH/Creating+and+running+a+Python+unit+test

from unittest import TestCase
from Fizzbuzz import Fizzbuzz

class TestFizzbuzz(TestCase):

    def test_get_fizzbuzz(self):
        f = Fizzbuzz()
        self.assertEqual(f.get_fizzbuzz_string(15),"Fizzbuzz")

    def test_get_fizz(self):
        f = Fizzbuzz()
        self.assertEqual(f.get_fizzbuzz_string(6), "Fizz")

    def test_get_buzz(self):
        f = Fizzbuzz()
        self.assertEqual(f.get_fizzbuzz_string(10), "Buzz")

    def test_get_empty(self):
        f = Fizzbuzz()
        self.assertEqual(f.get_fizzbuzz_string(8675309), "")