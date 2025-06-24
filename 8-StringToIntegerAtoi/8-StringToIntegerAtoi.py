# Last updated: 6/25/2025, 4:12:29 AM
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespaces
        if not s:
            return 0
        
        sign = 1
        result = 0
        index = 0
        
        # Check the sign
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        # Convert the digits
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        result *= sign
        
        # Clamp result to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
