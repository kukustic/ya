import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_cir(self):
        areacir = area(0)
        perimetercir = perimeter(0)
        self.assertEqual(areacir, 0)
        self.assertEqual(perimetercir, 0)



if __name__ == '__main__':
    unittest.main()
