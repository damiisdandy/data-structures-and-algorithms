import unittest
from .three_sum import threeSum


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_case2(self):
        self.assertEqual(threeSum([0, 1, 1]), [])

    def test_case3(self):
        self.assertEqual(threeSum([0, 0, 0]), [[0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
