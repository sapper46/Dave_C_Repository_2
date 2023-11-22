from unittest import TestCase
from TCSS_502_Assignment_4_Main import Circle
from TCSS_502_Assignment_4_Main import ShapeFactory
import math

class TestDrawingProgram(TestCase):
    def test_area(self):
        c = ShapeFactory.create_shape("Circle", 1)
        s = ShapeFactory.create_shape("Square", 1)
        r = ShapeFactory.create_shape("Rectangle", 1, 1)
        t = ShapeFactory.create_shape("Triangle", 1, 1)
        self.assertEqual(c.area(), 3.14159)
        self.assertEqual(s.area(), 1)
        self.assertEqual(r.area(), 1)
        self.assertEqual(t.area(), .5)

    def test_perimeter(self):
        c = ShapeFactory.create_shape("Circle", 1)
        s = ShapeFactory.create_shape("Square", 1)
        r = ShapeFactory.create_shape("Rectangle", 1, 1)
        t = ShapeFactory.create_shape("Triangle", 1, 1)
        self.assertEqual(c.perimeter(), 3.14159*2)
        self.assertEqual(s.perimeter(), 4)
        self.assertEqual(r.perimeter(), 4)
        self.assertEqual(t.perimeter(), math.sqrt(6))

    def test_eq_lt_gt(self):
        c = ShapeFactory.create_shape("Circle", 1)
        s = ShapeFactory.create_shape("Square", 4)
        r = ShapeFactory.create_shape("Rectangle", 4, 4)
        t = ShapeFactory.create_shape("Triangle", 4, 4)
        self.assertLess(c,s)
        self.assertGreater(s,r)
        self.assertEqual(t,t)





