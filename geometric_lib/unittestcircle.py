import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_cir(self):
        areacir = area(0)
        perimetercir = perimeter(0)
        self.assertEqual(areacir, 0)
        self.assertEqual(perimetercir, 0)

    def test_per_cir(self):
        perimetercir = perimeter(20)
        self.assertEqual(perimetercir, 125.66370614359172)

    def test_area_cir(self):
        areacir = area(17)
        self.assertEqual(areacir, 907.9202768874503)

if __name__ == '__main__':
    unittest.main()