import math
import unittest

from unittest.mock import call, patch

from exercises.basics import *

class TestBasics(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(8, 5), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)

    def test_in_fahrenheit(self):
        self.assertEqual(inFahrenheit(0), 32)

    def test_in_celsius(self):
        self.assertEqual(inCelsius(32), 0)
        self.assertAlmostEqual(inCelsius(0), -17.77777777777778)

    def test_umsatzsteuer_2005_18k(self):
        self.assertEqual(umsatzsteuer(18000, 2005), 3420)
    
    def test_umsatzsteuer_2020_10k(self):
        self.assertEqual(umsatzsteuer(10000, 2020), 0)

    def test_umsatzsteuer_2020_100k(self):
        self.assertEqual(umsatzsteuer(100000, 2020), 19000)

    def test_umsatzsteuer_2023_18k(self):
        self.assertEqual(umsatzsteuer(18000, 2023), 0)

    def test_area_of_unit_circle(self):
        self.assertAlmostEqual(area('circle', { 'radius': 1.0 }), math.pi)

    def test_area_of_triangle(self):
        self.assertEqual(area('triangle', { 'base': 2, 'height': 1.8 }), 1.8)

    def test_area_of_rectangle(self):
        self.assertEqual(area('rectangle', { 'base': 2, 'height': 1.8 }), 3.6)

    @patch('builtins.print')
    def test_fizzbuzz(self, mock_print):
        fizzbuzz(10)
        mock_print.assert_has_calls([
            call(1),
            call(2),
            call('fizz'),
            call(4),
            call('buzz'),
            call('fizz'),
            call(7),
            call(8),
            call('fizz'),
            call('buzz')
            ])

    def test_fibonacci(self):
        for n, m in [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (10, 55),
            (15, 610)
        ]:
            self.assertEqual(fibonacci(n), m)