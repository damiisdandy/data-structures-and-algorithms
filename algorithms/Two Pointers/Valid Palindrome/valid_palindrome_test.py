import unittest
from .valid_palindrome import isPalindrome


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(isPalindrome("A man, a plan, a canal: Panama"), True)

    def test_case2(self):
        self.assertEqual(isPalindrome("race a car"), False)

    def test_case3(self):
        self.assertEqual(isPalindrome(" "), True)


if __name__ == "__main__":
    unittest.main()
