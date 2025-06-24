# Last updated: 6/25/2025, 4:10:58 AM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        
        # Initialize the first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        # Fill in the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]
