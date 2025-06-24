# Last updated: 6/25/2025, 4:11:18 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:  # If n is odd
                result *= x
            x *= x
            n //= 2
        
        return result
