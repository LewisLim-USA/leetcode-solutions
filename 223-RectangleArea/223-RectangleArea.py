# Last updated: 6/25/2025, 4:10:30 AM
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                          bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_y = max(0, min(ay2, by2) - max(ay1, by1))
        overlap = overlap_x * overlap_y
        return area1 + area2 - overlap
