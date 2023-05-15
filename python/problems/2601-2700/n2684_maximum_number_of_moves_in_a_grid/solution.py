from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        print(grid)
        max_steps = len(grid[0]) - 1
        for c in range(1, len(grid[0])):
            ends = 0
            for r in range(0, len(grid)):
                prevs = [i for i in (
                    grid[max(r - 1, 0)][c - 1],
                    grid[r][c - 1],
                    grid[min(r + 1, len(grid) - 1)][c - 1],
                ) if i > -1]
                if not prevs or grid[r][c] <= min(prevs):
                    grid[r][c] = -1
                    ends += 1
            print(grid)
            if ends >= len(grid):
                max_steps = c - 1
                break

        print(grid)
        return max_steps
