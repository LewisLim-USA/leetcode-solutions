# Last updated: 6/25/2025, 4:10:03 AM
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Given a collection of intervals, find the minimum number of intervals you need to remove
        to make the rest of the intervals non-overlapping.

        Note:
        You may assume the interval's end point is always bigger than its start point.
        Intervals [1,2] and [2,3] are considered non-overlapping.

        Example 1:
        Input: [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

        Example 2:
        Input: [[1,2],[1,2],[1,2]]
        Output: 2
        Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

        Example 3:
        Input: [[1,2],[2,3]]
        Output: 0
        Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

        Constraints:
        1 <= len(intervals) <= 10^5
        intervals[i].length == 2
        -5 * 10^4 <= intervals[i][0] < intervals[i][1] <= 5 * 10^4
        """
        if not intervals:
            return 0

        # Sort the intervals by their end times.
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        count = 1  # Count of non-overlapping intervals

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if start >= end:
                # Current interval does not overlap with the previous non-overlapping interval
                count += 1
                end = intervals[i][1]

        # The number of intervals to remove is the total number of intervals minus the number of non-overlapping intervals.
        return len(intervals) - count