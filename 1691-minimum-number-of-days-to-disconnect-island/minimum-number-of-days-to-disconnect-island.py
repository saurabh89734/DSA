from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def count_islands():
            visited = [[False] * n for _ in range(m)]

            def dfs(r, c):
                visited[r][c] = True
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        grid[nr][nc] == 1 and
                        not visited[nr][nc]):
                        dfs(nr, nc)

            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)

            return islands

        if count_islands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2