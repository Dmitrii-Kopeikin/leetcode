from typing import List, Optional
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # collect all '0' cells
        queue = deque()
        
        for i in range(m):
            queue.extend([(i, j, 1) for j in range(n) if mat[i][j] == 0])

        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

        visited = set()
        while queue:
            y, x, distance = queue.pop()
            for dy, dx in DIRECTIONS:
                if 0 <= (ny := y + dy) < m and 0 <= (nx := x + dx) < n:
                    if (ny, nx) not in visited and mat[ny][nx] == 1:
                        visited.add((ny, nx))
                        mat[ny][nx] = distance
                        queue.appendleft((ny, nx, distance + 1))

        return mat
