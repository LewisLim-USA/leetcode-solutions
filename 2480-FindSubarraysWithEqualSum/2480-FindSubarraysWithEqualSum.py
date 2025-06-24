# Last updated: 6/25/2025, 4:09:21 AM
class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            curr_sum = nums[i] + nums[i + 1]
            if curr_sum in seen:
                return True
            seen.add(curr_sum)
        return False
