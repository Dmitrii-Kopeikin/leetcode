from typing import List


class Solution:
    def check_cell(self, x, y, grid, checked_grid):
        if checked_grid[y][x] == 1:
            return 0
        checked_grid[y][x] = 1

        if grid[y][x] == 1:
            result = 1
            if y > 0:
                result += self.check_cell(x, y - 1, grid, checked_grid)
            if y < len(grid) - 1:
                result += self.check_cell(x, y + 1, grid, checked_grid)
            if x > 0:
                result += self.check_cell(x - 1, y, grid, checked_grid)
            if x < len(grid[0]) - 1:
                result += self.check_cell(x + 1, y, grid, checked_grid)
            return result

        return 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid_checked = []
        for i in grid:
            grid_checked.append([0] * len(i))

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, self.check_cell(j, i, grid, grid_checked))

        return max_area
