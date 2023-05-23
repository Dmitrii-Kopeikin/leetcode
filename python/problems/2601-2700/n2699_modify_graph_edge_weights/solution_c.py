from math import inf
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def modifiedGraphEdges(
            self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:

        graph = [[] for _ in range(n)]
        for s, d, w in edges:
            graph[s].append([d, w])
            graph[d].append([s, w])

        # print(graph)

        def dijkstra(source: int, graph: list[list[int]], skip_negative: bool):
            pq = [[0, source]]
            dist = defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in graph[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heappush(pq, [d2, nei])
            return dist, parent

        print(dijkstra(destination, graph, skip_negative=True))
        print(dijkstra(destination, graph, skip_negative=False))