# Last updated: 6/25/2025, 4:11:26 AM
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(n - 1):  # We don't need to jump from the last index
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
