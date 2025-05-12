# Last updated: 5/12/2025, 9:46:59 AM
class Solution:
    def twoSum(self, numbers, target):
        i = 0                      # Start pointer at the beginning
        j = len(numbers) - 1       # End pointer at the end

        while i < j:               # Keep checking while pointers don't cross
            total = numbers[i] + numbers[j]  # Add the two pointed values
            if total == target:              # If they match the target
                return [i + 1, j + 1]         # Return 1-indexed positions
            if total < target:               # If sum is too small
                i += 1                        # Move start pointer right
            else:                             # If sum is too big
                j -= 1                        # Move end pointer left
