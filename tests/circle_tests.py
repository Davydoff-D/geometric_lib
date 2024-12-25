import unittest
import circle
import math

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(4), 50.26548245743669)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(4), 12.566370614359172)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_area_inf(self):
        self.assertRaises(ValueError, circle.area, math.inf)

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, circle.perimeter, math.inf)

    def test_area_negative(self):
        self.assertRaises(ValueError, circle.area, -2)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, circle.perimeter, -2)
