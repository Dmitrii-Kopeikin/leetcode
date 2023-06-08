from typing import List, Optional


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

        m = len(grid2)
        n = len(grid2[0])

        def dfs(y, x):
            nonlocal result
            if grid2[y][x] == 1:
                if grid1[y][x] == 0:
                    result = False
                grid2[y][x] = 0
                for (dy, dx) in DIRECTIONS:
                    if 0 <= dy + y < m and 0 <= dx + x < n:
                        dfs(dy + y, dx + x)

        counter = 0
        for y in range(m):
            for x in range(n):
                if grid2[y][x] == 1:
                    result = True
                    dfs(y, x)
                    counter += int(result)

        return counter
