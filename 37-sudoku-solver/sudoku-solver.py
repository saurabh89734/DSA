class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize constraints
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def backtrack(index):
            # All empty cells filled
            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + c // 3

            for num in "123456789":
                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box]
                ):
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo choice
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0)