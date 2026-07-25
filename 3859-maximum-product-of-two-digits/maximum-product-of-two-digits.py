class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        ans = 0
        m = len(digits)

        for i in range(m):
            for j in range(i + 1, m):
                ans = max(ans, digits[i] * digits[j])

        return ans