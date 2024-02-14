import unittest
from .valid_sudoku import isValidSudoku


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(
            isValidSudoku(
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ),
            True,
        )

    def test_case2(self):
        self.assertEqual(
            isValidSudoku(
                [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ),
            False,
        )

    def test_case3(self):
        self.assertEqual(
            isValidSudoku(
                [
                    [".", ".", ".", ".", "5", ".", ".", "1", "."],
                    [".", "4", ".", "3", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                    [".", ".", "2", ".", "7", ".", ".", ".", "."],
                    [".", "1", "5", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", "2", ".", ".", "."],
                    [".", "2", ".", "9", ".", ".", ".", ".", "."],
                    [".", ".", "4", ".", ".", ".", ".", ".", "."],
                ]
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
