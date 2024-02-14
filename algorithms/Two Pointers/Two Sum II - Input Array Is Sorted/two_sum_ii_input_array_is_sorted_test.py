import unittest
from .two_sum_ii_input_array_is_sorted import twoSum


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_case2(self):
        self.assertEqual(twoSum([2, 3, 4], 6), [1, 3])

    def test_case3(self):
        self.assertEqual(twoSum([-1, 0], -1), [1, 2])


if __name__ == "__main__":
    unittest.main()
