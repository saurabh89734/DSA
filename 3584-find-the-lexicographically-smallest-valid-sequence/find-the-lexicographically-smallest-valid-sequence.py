class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = last index in word1 where word2[j] occurs
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        # required by the problem
        tenvoraliq = (word1, word2)

        ans = []
        j = 0
        mismatch = True

        for i in range(n):

            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one allowed mismatch
            elif mismatch:
                # Can remaining characters of word2 be matched?
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    mismatch = False

        if j == m:
            return ans

        return []