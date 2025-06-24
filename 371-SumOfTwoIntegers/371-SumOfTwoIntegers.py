# Last updated: 6/25/2025, 4:10:26 AM
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        return a if a <= MAX else ~(a ^ MASK)
