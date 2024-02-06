import unittest
from .longest_consecutive_sequence import longestConsecutive


class TestArray(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_case2(self):
        self.assertEqual(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)


if __name__ == "__main__":
    unittest.main()
