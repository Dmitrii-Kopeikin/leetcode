from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 200 is max input value by constraints.
        memo = [[201] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                memo[i][j] = grid[i][j] + (min(memo[i][j-1], memo[i-1][j]) if i or j else 0)

        return memo[m-1][n-1]
