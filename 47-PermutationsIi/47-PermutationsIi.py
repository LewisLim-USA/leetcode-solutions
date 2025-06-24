# Last updated: 6/25/2025, 4:11:23 AM
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()  # Sort to easily detect duplicates

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: if the current number is the same as the previous and the previous was not used
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
