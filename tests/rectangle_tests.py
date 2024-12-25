import unittest
import rectangle
import math

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(10, 5), 50)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_area_inf(self):
        self.assertRaises(ValueError, rectangle.area, math.inf, 3)

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, rectangle.perimeter, math.inf, 3)

    def test_area_negative(self):
        self.assertRaises(ValueError, rectangle.area, -2, 3)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, rectangle.perimeter, -2, 3)