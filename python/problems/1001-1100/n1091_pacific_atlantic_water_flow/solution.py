from typing import List, Optional
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if 1 in (grid[0][0], grid[n - 1][n - 1]):
            return -1
        elif n == 1:
            return 1

        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1))

        queue = deque([(0, 0)])
        next_queue = deque()
        visited = set([(0, 0)])

        shortest_distance = 2
        while queue or next_queue:
            (i, j) = queue.pop()
            for di, dj in DIRECTIONS:
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < n and 0 <= next_j < n and (next_i, next_j) not in visited:
                    if next_i == n - 1 and next_j == n - 1:
                        return shortest_distance
                    if grid[next_i][next_j] == 0:
                        next_queue.appendleft((next_i, next_j))
                    visited.add((next_i, next_j))
            if not queue:
                shortest_distance += 1
                queue, next_queue = next_queue, queue

        return -1
