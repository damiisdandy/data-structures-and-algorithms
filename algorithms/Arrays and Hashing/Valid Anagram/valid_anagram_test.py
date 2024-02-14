import unittest
from .valid_anagram import isAnagram


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(isAnagram("anagram", "nagaram"), True)

    def test_case2(self):
        self.assertEqual(isAnagram("rat", "cat"), False)


if __name__ == "__main__":
    unittest.main()
