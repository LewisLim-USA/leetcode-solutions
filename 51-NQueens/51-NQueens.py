# Last updated: 6/25/2025, 4:11:17 AM
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        def backtrack(row, cols, diag1, diag2, board):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                backtrack(row + 1, cols, diag1, diag2, board)

                # Backtrack
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
