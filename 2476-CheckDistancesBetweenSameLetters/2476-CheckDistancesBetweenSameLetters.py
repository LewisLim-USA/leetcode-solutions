# Last updated: 6/25/2025, 4:09:23 AM
class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first_occurrence = {}

        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            else:
                expected_distance = distance[ord(char) - ord('a')]
                actual_distance = i - first_occurrence[char] - 1
                if actual_distance != expected_distance:
                    return False
        return True
