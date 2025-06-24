# Last updated: 6/25/2025, 4:10:04 AM
class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0

        segments = 0
        in_segment = False
        for char in s:
            if char != ' ':
                if not in_segment:
                    segments += 1
                    in_segment = True
            else:
                in_segment = False
        return segments