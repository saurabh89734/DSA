class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = whether s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Patterns like a*, a*b*, a*b*c* can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Direct character match or '.'
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == '*':
                    # Zero occurrences of preceding character
                    dp[i][j] = dp[i][j - 2]

                    # One or more occurrences
                    prev = p[j - 2]
                    if prev == '.' or prev == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]