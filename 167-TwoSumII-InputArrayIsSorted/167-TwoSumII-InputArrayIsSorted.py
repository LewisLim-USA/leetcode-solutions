# Last updated: 5/12/2025, 9:46:16 AM
class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]  # 1-indexed
            if total < target:
                i += 1
            else:
                j -= 1