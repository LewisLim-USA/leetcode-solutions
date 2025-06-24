# Last updated: 6/25/2025, 4:11:11 AM
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True
