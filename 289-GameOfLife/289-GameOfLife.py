# Last updated: 6/25/2025, 4:10:27 AM
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Models a sensor grid, like soil moisture or light sensors evolving states
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                live = 0
                for dx, dy in directions:
                    if 0 <= i+dx < m and 0 <= j+dy < n and abs(board[i+dx][j+dy]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1  # was alive, now dead
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2   # was dead, now alive

        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
