class Solution:
    def outerTrees(self, trees):

        if len(trees) <= 3:
            return trees

        trees.sort()

        def cross(a, b, c):
            return (
                (b[0] - a[0]) * (c[1] - a[1])
                - (b[1] - a[1]) * (c[0] - a[0])
            )

        # Lower hull
        lower = []

        for point in trees:

            while (
                len(lower) >= 2
                and cross(lower[-2], lower[-1], point) < 0
            ):
                lower.pop()

            lower.append(point)

        # Upper hull
        upper = []

        for point in reversed(trees):

            while (
                len(upper) >= 2
                and cross(upper[-2], upper[-1], point) < 0
            ):
                upper.pop()

            upper.append(point)

        # Remove duplicate corner points
        hull = lower[:-1] + upper[:-1]

        return [list(point) for point in set(map(tuple, hull))]