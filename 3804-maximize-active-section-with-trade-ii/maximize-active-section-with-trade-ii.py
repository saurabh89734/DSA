from dataclasses import dataclass
from itertools import pairwise


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        self.st = [[0] * (n + 1) for _ in range(n.bit_length() + 1)]
        if n:
            self.st[0][:n] = nums

            for k in range(1, n.bit_length() + 1):
                for i in range(n - (1 << k) + 1):
                    self.st[k][i] = max(
                        self.st[k - 1][i],
                        self.st[k - 1][i + (1 << (k - 1))]
                    )

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        ones = s.count("1")

        zeroGroups, zeroGroupIndex = self._getZeroGroups(s)

        if not zeroGroups:
            return [ones] * len(queries)

        mergeLengths = self._getMergeLengths(zeroGroups)
        st = SparseTable(mergeLengths)

        ans = []

        for l, r in queries:

            if zeroGroupIndex[l] == -1:
                left = -1
            else:
                g = zeroGroups[zeroGroupIndex[l]]
                left = g.length - (l - g.start)

            if zeroGroupIndex[r] == -1:
                right = -1
            else:
                g = zeroGroups[zeroGroupIndex[r]]
                right = r - g.start + 1

            startPair = zeroGroupIndex[l] + 1
            endGroup = zeroGroupIndex[r] if s[r] == "1" else zeroGroupIndex[r] - 1
            endPair = endGroup - 1

            best = ones

            if (
                s[l] == "0"
                and s[r] == "0"
                and zeroGroupIndex[l] + 1 == zeroGroupIndex[r]
            ):
                best = max(best, ones + left + right)

            elif startPair <= endPair:
                best = max(best, ones + st.query(startPair, endPair))

            if (
                s[l] == "0"
                and zeroGroupIndex[l] + 1
                <= (zeroGroupIndex[r] if s[r] == "1" else zeroGroupIndex[r] - 1)
            ):
                best = max(
                    best,
                    ones + left + zeroGroups[zeroGroupIndex[l] + 1].length,
                )

            if (
                s[r] == "0"
                and zeroGroupIndex[l] < zeroGroupIndex[r] - 1
            ):
                best = max(
                    best,
                    ones + right + zeroGroups[zeroGroupIndex[r] - 1].length,
                )

            ans.append(best)

        return ans

    def _getZeroGroups(self, s):
        groups = []
        idx = []

        for i, ch in enumerate(s):
            if ch == "0":
                if i > 0 and s[i - 1] == "0":
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)

        return groups, idx

    def _getMergeLengths(self, groups):
        return [a.length + b.length for a, b in pairwise(groups)]