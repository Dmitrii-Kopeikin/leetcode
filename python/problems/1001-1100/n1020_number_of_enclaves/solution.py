from typing import List, Optional


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def check_cell(x, y):
            if grid[y][x] == -1:
                return False
            if grid[y][x] in (0, 2) :
                return True
            
            checked_stack.append((x, y))

            result = True
            for dir_x, dir_y in DIRECTIONS:
                n_x = dir_x + x
                n_y = dir_y + y
                if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                    if (n_x, n_y) not in checked_stack:
                        result = result and check_cell(n_x, n_y)
                else:
                    result = False

            if not result:
                grid[y][x] = -1

            return result

        enclaves = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] in (1, 2):
                    checked_stack = []
                    is_enclave = check_cell(x, y)
                    if is_enclave:
                        enclaves += 1
                    while checked_stack:
                        (xx, yy) = checked_stack.pop()
                        grid[yy][xx] = 2 if is_enclave else -1

        return enclaves
