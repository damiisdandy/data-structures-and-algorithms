import unittest
from .trapping_rain_water import trap


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_case2(self):
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)


if __name__ == "__main__":
    unittest.main()
