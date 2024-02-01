import unittest
from .top_k_frequent_elements import topKFrequent


class TestArray(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_case2(self):
        self.assertEqual(topKFrequent([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
