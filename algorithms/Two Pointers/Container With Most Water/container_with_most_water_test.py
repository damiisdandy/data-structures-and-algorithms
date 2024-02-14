import unittest
from .container_with_most_water import maxArea


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_case2(self):
        self.assertEqual(maxArea([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
