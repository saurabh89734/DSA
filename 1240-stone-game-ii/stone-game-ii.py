class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, m):
            if i >= n:
                return 0

            if (i, m) in dp:
                return dp[(i, m)]

            # Can take everything
            if i + 2 * m >= n:
                return suffix[i]

            best = 0

            for x in range(1, 2 * m + 1):
                # Remaining stones after taking x
                opponent = solve(i + x, max(m, x))

                # Total remaining - opponent's best
                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, m)] = best
            return best

        return solve(0, 1)