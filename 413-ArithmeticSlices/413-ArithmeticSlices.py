# Last updated: 6/25/2025, 4:10:22 AM
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        current = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current += 1
                count += current
            else:
                current = 0
        
        return count
