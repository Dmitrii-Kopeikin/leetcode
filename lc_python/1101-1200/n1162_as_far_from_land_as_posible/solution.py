from typing import List, Optional
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((0, 1), (1, 0), (-1, 0), (0, -1))

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    queue.appendleft((y, x))

        if not queue or len(queue) == m * n:
            return -1

        max_distance = 0
        next_queue = deque()
        while queue or next_queue:
            if not queue:
                queue, next_queue = next_queue, queue
                max_distance += 1
            y, x = queue.pop()
            for next_y, next_x in DIRECTIONS:
                if 0 <= (next_y := next_y + y) < m and 0 <= (next_x := next_x + x) < n:
                    if grid[next_y][next_x] == 0:
                        grid[next_y][next_x] = 1
                        next_queue.appendleft((next_y, next_x))

        return max_distance
