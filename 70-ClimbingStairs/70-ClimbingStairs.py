# Last updated: 6/25/2025, 4:12:41 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # a = ways to climb to (n-2), b = ways to climb to (n-1)
        for _ in range(3, n + 1):
            a, b = b, a + b  # like Fibonacci sequence
        return b
