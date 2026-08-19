class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for r, seat in reservedSeats:
            if r not in rows:
                rows[r] = set()

            rows[r].add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                ans += 2

            elif left or right:
                ans += 1

            elif all(seat not in seats for seat in [4, 5, 6, 7]):
                ans += 1

        return ans