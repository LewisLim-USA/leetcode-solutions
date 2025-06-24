# Last updated: 6/25/2025, 4:09:33 AM
from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        result = []

        for i in range(len(num) - 1, -1, -1):
            carry += num[i]
            result.append(carry % 10)
            carry //= 10

        while carry > 0:
            result.append(carry % 10)
            carry //= 10

        return result[::-1]

