from collections import defaultdict


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    row_hash = defaultdict(set)
    column_hash = defaultdict(set)
    square_hash = defaultdict(set)

    for r in range(9):
        for c in range(9):
            # to group each mini 3 x 3 square e.g
            # for cells
            # 0,2 => (0, 0)
            # 0,5 => (0, 1)
            # 7,8 => (2, 2)
            # you will notice that they appear on those index positions for the subdivided board
            mini_square_id = (r // 3, c // 3)
            cell = board[r][c]
            if cell == ".":
                continue
            if (
                cell in row_hash[r]
                or cell in column_hash[c]
                or cell in square_hash[mini_square_id]
            ):
                return False
            else:
                row_hash[r].add(cell)
                column_hash[c].add(cell)
                square_hash[mini_square_id].add(cell)
    return True


# O(n^2)
