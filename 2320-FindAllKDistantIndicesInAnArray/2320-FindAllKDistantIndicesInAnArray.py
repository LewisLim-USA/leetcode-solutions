# Last updated: 6/25/2025, 4:09:29 AM
class Solution:
    def findKDistantIndices(self, nums, key, k):
        result = set()
        key_indices = [i for i, val in enumerate(nums) if val == key]
        
        for j in key_indices:
            for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                result.add(i)
        
        return sorted(result)
