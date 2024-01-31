import unittest
from .contains_duplicate import containsDuplicate


class TestArray(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(containsDuplicate([1, 2, 3, 1]), True)

    def test_case2(self):
        self.assertEqual(containsDuplicate([1, 2, 3, 4]), False)

    def test_case3(self):
        self.assertEqual(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == "__main__":
    unittest.main()
