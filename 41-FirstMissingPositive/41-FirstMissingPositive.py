# Last updated: 6/25/2025, 4:11:35 AM
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its right spot
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Find the first missing number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all numbers are in place
        return n + 1
