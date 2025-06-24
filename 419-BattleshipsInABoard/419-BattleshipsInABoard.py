# Last updated: 6/25/2025, 4:10:15 AM
from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        
        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # Check if it's the start of a new battleship
                    if (r == 0 or board[r-1][c] != 'X') and (c == 0 or board[r][c-1] != 'X'):
                        count += 1
        return count
