# Last updated: 6/25/2025, 4:12:35 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0

        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # final length

        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)       # odd-length palindrome
            len2 = expandAroundCenter(i, i + 1)   # even-length palindrome
            max_len = max(len1, len2)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
