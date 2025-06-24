# Last updated: 6/25/2025, 4:09:36 AM
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def overlap(x_shift, y_shift):
            count = 0
            for i in range(n):
                for j in range(n):
                    i2, j2 = i + y_shift, j + x_shift
                    if 0 <= i2 < n and 0 <= j2 < n and img1[i2][j2] == 1 and img2[i][j] == 1:
                        count += 1
            return count

        max_overlap = 0
        for y_shift in range(-n + 1, n):
            for x_shift in range(-n + 1, n):
                max_overlap = max(max_overlap, overlap(x_shift, y_shift))
        return max_overlap
