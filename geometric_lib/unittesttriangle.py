import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_tri(self):
        areatri = area(100, 0)
        perimetertri = perimeter(0, 0, 0)
        self.assertEqual(areatri, 0)
        self.assertEqual(perimetertri, 0)

    def test_per_tri(self):
        perimetertri = perimeter(20, 5, 10)
        self.assertEqual(perimetertri, 35)

    def test_area_tri(self):
        areatri = area(17, 10)
        self.assertEqual(areatri, 85)

if __name__ == '__main__':
    unittest.main()