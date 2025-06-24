# Last updated: 6/25/2025, 4:10:34 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dfs(i+x, j+y)
                return 1
            return 0
        return sum(dfs(i, j) for i in range(m) for j in range(n))
