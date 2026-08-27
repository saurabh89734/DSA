class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:

                # left character skip
                x, y = l + 1, r
                while x < y and s[x] == s[y]:
                    x += 1
                    y -= 1

                if x >= y:
                    return True

                # right character skip
                x, y = l, r - 1
                while x < y and s[x] == s[y]:
                    x += 1
                    y -= 1

                return x >= y

            l += 1
            r -= 1

        return True