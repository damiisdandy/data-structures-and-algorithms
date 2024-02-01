import unittest
from .product_of_array_except_self import productExceptSelf


class TestArray(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_case2(self):
        self.assertEqual(productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


if __name__ == "__main__":
    unittest.main()
