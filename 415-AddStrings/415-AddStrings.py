# Last updated: 5/12/2025, 12:27:19 PM
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        digits = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            digits.append(chr(carry % 10 + ord('0')))
            carry //= 10

        return ''.join(reversed(digits))
