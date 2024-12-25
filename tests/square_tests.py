import unittest
import square
import math

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)
    
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_area_inf(self):
        self.assertRaises(ValueError, square.area, math.inf)

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, square.perimeter, math.inf)

    def test_area_negative(self):
        self.assertRaises(ValueError, square.area, -2)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, square.perimeter, -2)
