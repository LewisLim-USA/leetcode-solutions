# Last updated: 5/12/2025, 9:52:19 AM
# Pattern: Hashmap
# Reason: Searching for complements in array
# Time: O(n), Space: O(n)
# Tip: Watch out for duplicates

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False