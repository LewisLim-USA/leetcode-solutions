# Last updated: 6/25/2025, 4:11:49 AM
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Start with -1 to handle edge cases
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len

        