class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], idx]
            lookup[num] = idx
