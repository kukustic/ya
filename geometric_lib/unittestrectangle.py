import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_rec(self):
        arearec = area(100, 0)
        perimeterec = perimeter(0, 0)
        self.assertEqual(arearec, 0)
        self.assertEqual(perimeterec, 0)

    def test_per_rec(self):
        perimeterec = perimeter(20, 5)
        self.assertEqual(perimeterec, 50)

    def test_area_rec(self):
        arearec = area(17, 10)
        self.assertEqual(arearec, 170)

if __name__ == '__main__':
    unittest.main()