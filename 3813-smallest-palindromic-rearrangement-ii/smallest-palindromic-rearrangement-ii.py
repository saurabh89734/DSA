from collections import Counter
from math import comb

class Solution:
    LIMIT = 10 ** 6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for c, v in cnt.items():
            half[ord(c) - ord('a')] = v // 2
            if v & 1:
                mid = c

        def ways(freq):
            """Number of distinct permutations of multiset."""
            total = sum(freq)
            ans = 1
            rem = total
            for f in freq:
                if f:
                    ans *= comb(rem, f)
                    if ans >= self.LIMIT:
                        return self.LIMIT
                    rem -= f
            return ans

        totalWays = ways(half)
        if totalWays < k:
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                cur = ways(half)

                if cur >= k:
                    left.append(chr(i + ord('a')))
                    break

                k -= cur
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]