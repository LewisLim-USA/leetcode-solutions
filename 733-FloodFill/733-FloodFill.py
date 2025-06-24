# Last updated: 6/25/2025, 4:09:49 AM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        def dfs(i, j):
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == original:
                image[i][j] = color
                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dfs(i+x, j+y)
        dfs(sr, sc)
        return image
