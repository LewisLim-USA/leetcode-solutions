# Last updated: 6/25/2025, 4:10:17 AM
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visited or 
                heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # DFS from Pacific Ocean
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])        # Left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])        # Top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row

        result = list(pacific & atlantic)
        return [list(cell) for cell in result]
