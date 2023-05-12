class Solution:
    def _check_cell(self, x, y, grid, checked_grid):
        if checked_grid[y][x] == 1:
            return 0
        checked_grid[y][x] = 1

        if grid[y][x] == '1':
            if y > 0:
                self._check_cell(x, y - 1, grid, checked_grid)
            if y < len(grid) - 1:
                self._check_cell(x, y + 1, grid, checked_grid)
            if x > 0:
                self._check_cell(x - 1, y, grid, checked_grid)
            if x < len(grid[0]) - 1:
                self._check_cell(x + 1, y, grid, checked_grid)
            return 1

        return 0

    def num_islands(self, grid: list[list[str]]) -> int:

        grid_checked = []
        for i in grid:
            grid_checked.append([0] * len(i))

        islands_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                islands_count += self._check_cell(j, i, grid, grid_checked)

        return islands_count
