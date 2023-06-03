from typing import List, Optional
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited_node = []
        queue = deque()

        for i in range(len(graph)):
            visited_node.append(set([1 << i]))
            queue.appendleft((i, 1 << i, 1))

        while queue:
            node, value, step = queue.pop()
            for neighbour_node in graph[node]:
                mid_node = (1 << neighbour_node) | value
                if mid_node not in visited_node[neighbour_node]:
                    if mid_node + 1 == 1 << len(graph):
                        return step
                    visited_node[neighbour_node].add(mid_node)
                    queue.appendleft ((neighbour_node, mid_node, step + 1))

        return 0
