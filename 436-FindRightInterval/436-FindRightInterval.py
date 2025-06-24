# Last updated: 6/25/2025, 4:10:01 AM
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Map each interval's start to its original index
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = []
        
        for interval in intervals:
            target = interval[1]  # We need to find the smallest start >= end
            idx = bisect_left(starts, (target,))  # Binary search
            if idx < len(starts):
                res.append(starts[idx][1])  # Append original index of the found interval
            else:
                res.append(-1)  # No such interval found
        return res

