from typing import List, Optional
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])

        pacific_set = {(heights[0][i], (0, i)) for i in range(n)}.union({(heights[i][0], (i, 0)) for i in range(1, m)})
        atlantic_set = {(heights[m - 1][i], (m - 1, i)) for i in range(n)}.union({(heights[i][n - 1], (i, n - 1)) for i in range(0, m - 1)})
        
        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def collect_heights(ocean_set: set, heights: list[list[int]]):
            queue = deque(ocean_set)
            while queue:
                height, (i, j) = queue.pop()
                for di, dj in DIRECTIONS:
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < m and 0 <= next_j < n:
                        h = heights[next_i][next_j]
                        if (h, (next_i, next_j)) not in ocean_set and h >= height:
                            ocean_set.add((h, (next_i, next_j)))
                            queue.appendleft((h, (next_i, next_j)))

        collect_heights(pacific_set, heights)
        collect_heights(atlantic_set, heights)
        
        return [list(i[1]) for i in pacific_set.intersection(atlantic_set)]
