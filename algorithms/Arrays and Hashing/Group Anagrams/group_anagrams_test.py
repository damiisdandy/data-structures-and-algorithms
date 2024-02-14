import unittest
from .group_anagrams import groupAnagrams


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(
            groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [
                [
                    "eat",
                    "tea",
                    "ate",
                ],
                ["tan", "nat"],
                ["bat"],
            ],
        )

    def test_case2(self):
        self.assertEqual(groupAnagrams([""]), [[""]])

    def test_case3(self):
        self.assertEqual(groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
