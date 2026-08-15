class Solution:
    def maximumSwap(self, num: int) -> int:

        digits = list(str(num))
        n = len(digits)

        # Last occurrence of every digit
        last = [0] * 10

        for i in range(n):
            last[int(digits[i])] = i

        # Find first digit that can be replaced
        for i in range(n):

            for d in range(9, int(digits[i]), -1):

                if last[d] > i:
                    digits[i], digits[last[d]] = (
                        digits[last[d]],
                        digits[i]
                    )

                    return int("".join(digits))

        return num