from typing import List, Optional
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

        queue = deque([(entrance[0], entrance[1], 1)])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            y, x, dist = queue.pop()
            for dy, dx in DIRECTIONS:
                if (
                    0 <= (ny := y + dy) < m
                    and 0 <= (nx := x + dx) < n
                    and maze[ny][nx] == '.'
                ):
                    if ny in [0, m - 1] or nx in [0, n - 1]:
                        return dist
                    maze[ny][nx] = "+"
                    queue.appendleft((ny, nx, dist + 1))

        return -1
