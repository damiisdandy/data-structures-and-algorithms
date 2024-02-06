import unittest
from .string_encode_and_decode import Solution


class TestArray(unittest.TestCase):
    def test_case1(self):
        strs = ["neet", "code", "love", "you"]
        solution = Solution()
        encoded_string = solution.encode(strs)
        result = solution.decode(encoded_string)
        self.assertEqual(strs, result)

    def test_case2(self):
        strs = ["we", "say", ":", "yes", "😊5"]
        solution = Solution()
        encoded_string = solution.encode(strs)
        result = solution.decode(encoded_string)
        self.assertEqual(strs, result)


if __name__ == "__main__":
    unittest.main()
