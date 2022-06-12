# Using backtracking and bounding function to find all the correct possibilities of arranging queens.

# We will need to maintain state of the board, column, pos_diag and neg_diag. No need to maintain state
# for row as we will iterate through it using the recursive calls. If the column, pos_diag or neg_diag
# of the queen we are looking at has already been seen then no need to process anymore as it is not
# valid.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]
        result = []

        def backtracking(r):
            if r == n:
                res_board = ["".join(board[row]) for row in range(n)]
                result.append(res_board)
                return

            for c in range(n):
                # If invalid position then move on to the next column.
                if c in column or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue

                # Since position not invalid, update state of all sets and the board.
                column.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # Recursively call backtracking for the next queen.
                backtracking(r + 1)

                # Since we are done with checking if solution exists or not, we now need to backtrack and remove
                # old states.
                column.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtracking(0)
        return result