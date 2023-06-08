from typing import List, Optional
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((0, 1), (1, 0), (-1, 0), (0, -1))

        m = len(grid)
        n = len(grid[0])

        def find_island(y: int, x: int, island: list):
            if grid[y][x] == 1:
                island.append((y, x))
            
            for next_y, next_x in DIRECTIONS:
                if 0 <= (next_y := next_y + y) < m and 0 <= (next_x := next_x + x) < n:
                    if grid[y][x] == 1 and (next_y, next_x) not in island:
                        find_island(next_y, next_x, island)

            return
        
        def find_bridge_length(queue: deque):
            visited = set(queue)
            next_queue = deque()
            distance = 0
            while queue or next_queue:
                if not queue:
                    queue, next_queue = next_queue, queue
                    distance += 1
                y, x = queue.pop()
                for next_y, next_x in DIRECTIONS:
                    if 0 <= (next_y := next_y + y) < m and 0 <= (next_x := next_x + x) < n:
                        if (next_y, next_x) in visited:
                            continue
                        visited.add((next_y, next_x))
                        if grid[next_y][next_x] == 1:
                            return distance
                        next_queue.appendleft((next_y, next_x))
            
            return - 1


        island = deque()
        for y in range(m):
            if not island:
                for x in range(n):
                    if grid[y][x] == 1:
                        find_island(y, x, island)
                        break

        return find_bridge_length(island)
        

       
        

    