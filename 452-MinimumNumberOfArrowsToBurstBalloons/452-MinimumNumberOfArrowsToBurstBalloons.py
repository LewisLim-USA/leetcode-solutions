# Last updated: 6/25/2025, 4:09:58 AM
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons by their end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for start, end in points[1:]:
            if start > current_end:
                arrows += 1
                current_end = end

        return arrows
