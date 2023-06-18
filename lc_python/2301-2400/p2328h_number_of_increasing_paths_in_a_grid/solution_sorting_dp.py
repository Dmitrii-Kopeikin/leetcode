from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

        m = len(grid)
        n = len(grid[0])

        dp = [[1] * n for _ in range(m)]

        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda x: grid[x[0]][x[1]])

        for (i, j) in cells:
            for di, dj in DIRECTIONS:
                if 0 <= (ni := i + di) < m and 0 <= (nj := j + dj) < n and grid[ni][nj] > grid[i][j]:
                    dp[ni][nj] += dp[i][j]

        return sum(list(map(sum, dp))) % 1_000_000_007
