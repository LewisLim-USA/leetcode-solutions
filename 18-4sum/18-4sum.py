# Last updated: 6/25/2025, 4:12:11 AM
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates for the first number
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue  # Skip duplicates for the second number
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates for third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res
