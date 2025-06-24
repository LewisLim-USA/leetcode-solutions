# Last updated: 6/25/2025, 4:09:44 AM
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isLeaf(x1, y1, length):
            val = grid[x1][y1]
            for i in range(x1, x1 + length):
                for j in range(y1, y1 + length):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def build(x, y, length):
            leaf, val = isLeaf(x, y, length)
            if leaf:
                return Node(val == 1, True, None, None, None, None)

            half = length // 2
            return Node(
                True, False,
                build(x, y, half),
                build(x, y + half, half),
                build(x + half, y, half),
                build(x + half, y + half, half)
            )

        return build(0, 0, len(grid))
