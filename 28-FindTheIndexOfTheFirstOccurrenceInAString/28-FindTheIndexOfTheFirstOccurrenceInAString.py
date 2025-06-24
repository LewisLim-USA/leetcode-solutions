# Last updated: 6/25/2025, 4:11:56 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0
        
        # Loop through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
