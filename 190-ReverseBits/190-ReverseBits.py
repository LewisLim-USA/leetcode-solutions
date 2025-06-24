# Last updated: 6/25/2025, 4:10:31 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
