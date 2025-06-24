# Last updated: 6/25/2025, 4:10:09 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        count = [0] * 26  # For each uppercase English letter
        left = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1
            max_count = max(max_count, count[index])

            # If the remaining characters in the window (right - left + 1 - max_count) 
            # are more than k, shrink the window from the left
            if (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
