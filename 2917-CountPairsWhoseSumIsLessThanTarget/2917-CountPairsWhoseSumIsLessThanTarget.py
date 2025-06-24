# Last updated: 6/25/2025, 4:09:26 AM
class Solution:
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
