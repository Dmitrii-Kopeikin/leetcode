from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = 1

            for di, dj in DIRECTIONS:
                if 0 <= (ni := i + di) < m and 0 <= (nj := j + dj) < n and grid[ni][nj] < grid[i][j]:
                    dp[i][j] += dfs(ni, nj)

            return dp[i][j]
        
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % 1_000_000_007
