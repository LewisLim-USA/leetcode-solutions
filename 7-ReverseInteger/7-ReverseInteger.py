# Last updated: 6/25/2025, 4:12:30 AM
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1]) * sign

        # Check for 32-bit signed integer overflow
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x
