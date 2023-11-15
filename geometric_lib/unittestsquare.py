import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_squ(self):
        areasqu = area(0)
        perimetersqu = perimeter(0)
        self.assertEqual(areasqu, 0)
        self.assertEqual(perimetersqu, 0)

    def test_per_squ(self):
        perimetersqu = perimeter(20)
        self.assertEqual(perimetersqu, 80)

    def test_area_squ(self):
        areasqu = area(17)
        self.assertEqual(areasqu, 289)

if __name__ == '__main__':
    unittest.main()