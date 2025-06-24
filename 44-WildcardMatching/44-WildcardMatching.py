# Last updated: 6/25/2025, 4:11:30 AM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        # dp[i][j] = True if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        dp[0][0] = True  # empty string matches empty pattern
        
        # Handle patterns like "*", "**", etc.
        for j in range(1, m + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j-1] == '*':
                    # * matches empty (dp[i][j-1]) or one/more chars (dp[i-1][j])
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[n][m]

        