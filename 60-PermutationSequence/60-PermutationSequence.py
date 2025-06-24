# Last updated: 6/25/2025, 4:11:05 AM
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        numbers = list(range(1, n + 1))
        k -= 1  # convert to 0-based index
        result = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(str(numbers.pop(index)))
            k %= fact

        return ''.join(result)
