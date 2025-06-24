# Last updated: 6/25/2025, 4:11:40 AM
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = "1"
        for _ in range(n - 1):
            curr = ""
            i = 0
            while i < len(prev):
                count = 1
                while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                    i += 1
                    count += 1
                curr += str(count) + prev[i]
                i += 1
            prev = curr
        return prev
