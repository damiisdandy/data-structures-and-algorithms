import unittest
from .two_sum import twoSum


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_case2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_case3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
