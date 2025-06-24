# Last updated: 6/25/2025, 4:11:31 AM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                sum_ = mul + result[p2]

                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        # Skip leading zeros
        res = []
        for num in result:
            if not (len(res) == 0 and num == 0):
                res.append(str(num))
        return ''.join(res)

        