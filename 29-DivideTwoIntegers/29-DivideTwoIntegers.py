# Last updated: 6/25/2025, 4:11:54 AM
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Get the sign
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= temp + temp:
                temp += temp
                multiple += multiple
            dividend -= temp
            quotient += multiple
        
        if negative:
            quotient = -quotient
        
        return quotient
