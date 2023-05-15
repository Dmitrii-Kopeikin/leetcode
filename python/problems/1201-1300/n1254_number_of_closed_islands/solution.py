from typing import List


class Solution:
    def check_cell(self, x, y, grid, checked_grid):
        # print(x, y)
        if checked_grid[y][x] != -1:
            return checked_grid[y][x]

        if grid[y][x] == 1:
            checked_grid[y][x] = True
            return True

        checked_grid[y][x] = True
        if grid[y][x] == 0:
            result = True
            counter = 0
            if y > 0 and result and self.check_cell(x, y - 1, grid, checked_grid):
                counter += 1
            if y < len(grid) - 1 and result and self.check_cell(x, y + 1, grid, checked_grid):
                counter += 1
            if x > 0 and result and self.check_cell(x - 1, y, grid, checked_grid):
                counter += 1
            if x < len(grid[0]) - 1 and result and self.check_cell(x + 1, y, grid, checked_grid):
                counter += 1
            if counter != 4:
                checked_grid[y][x] = False

        
        return checked_grid[y][x]
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        grid_checked = []
        for i in grid:
            grid_checked.append([-1] * len(i))

        closed_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.check_cell(j, i, grid, grid_checked):
                    closed_islands += 1

        return closed_islands
