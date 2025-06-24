# Last updated: 6/25/2025, 4:11:06 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()  # Remove trailing spaces
        length = 0
        for char in reversed(s):
            if char == ' ':
                break
            length += 1
        return length
