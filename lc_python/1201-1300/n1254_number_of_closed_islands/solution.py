from typing import List


class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        grid_checked = []
        for i in grid:
            grid_checked.append([-1] * len(i))

        DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def check_cell(x, y):
            if grid_checked[y][x] != -1:
                return grid_checked[y][x]

            if grid[y][x] == 1:
                return True

            grid_checked[y][x] = True
            result = True
            for dir_x, dir_y in DIRECTIONS:
                n_x = dir_x + x
                n_y = dir_y + y
                if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                    result = result and check_cell(n_x, n_y)
                else:
                    result = False

            grid_checked[y][x] = result
            return grid_checked[y][x]

        closed_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and grid_checked[i][j] == -1:
                    closed_islands += check_cell(j, i)

        return closed_islands
