# Last updated: 6/25/2025, 4:12:27 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Convert the number to a string
        x_str = str(x)
        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]
