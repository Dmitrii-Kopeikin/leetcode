from typing import List, Optional
from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        COLORS = (1, 0)
        for s, d in redEdges:
            graph[s].append((d, 0))  # 0 for red edges
        for s, d in blueEdges:
            graph[s].append((d, 1))  # 1 for blue edges

        paths = [0] + [-1] * (n - 1)

        queue = deque([(d, c, 1) for d, c in graph[0]])
        visited = set()
        while(queue):
            dest, color, dist = queue.pop()
            if (dest, color) in visited:
                continue
            visited.add((dest, color))
            if paths[dest] == -1:
                paths[dest] = dist
            else:
                paths[dest] = min(paths[dest], dist)
            for n_dest, n_color in graph[dest]:
                if n_color == COLORS[color]:
                    queue.appendleft((n_dest, n_color, dist + 1))

        return paths

        # def dfs(destination: int, color: int, paths: list[int], distance: int, visited: set[tuple[int, int]]) -> None:
        #     nonlocal graph

        #     visited.add((destination, color))

        #     if paths[destination] == -1:
        #         paths[destination] = distance
        #     else:
        #         paths[destination] = min(distance, paths[destination])

        #     for d, c in graph[destination]:
        #         if c == COLORS[color] and (d, c) not in visited:
        #             dfs(d, c, paths, distance + 1, visited)

        # paths = [0] + [-1] * (n - 1)
        # for destination, color in graph[0]:
        #     dfs(destination, color, paths, 1, set())

        # return paths
