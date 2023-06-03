from typing import List, Optional
from collections import defaultdict
from collections import deque


class Solution:
    # def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    #     n = len(graph)
    #     graph = list(map(set, graph))
    #     reversed_graph = [set() for _ in range(n)]
    #     queue = deque()

    #     for node, children in enumerate(graph):
    #         if not children:
    #             queue.append(node)
    #         for j in children:
    #             reversed_graph[j].add(node)

    #     safe_nodes = [False] * n
    #     while queue:
    #         node = queue.pop()
    #         safe_nodes[node] = True
    #         for next_node in reversed_graph[node]:
    #             graph[next_node].remove(node)
    #             if not graph[next_node]:
    #                 queue.appendleft(next_node)
    
    #     return [i for i, r in enumerate(safe_nodes) if r]

    # WHITE-GRAY-BLACK DFS Algorithm
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            
            color[node] = GRAY
            for next_node in graph[node]:
                if color[next_node] == BLACK:
                    continue
                if color[next_node] == GRAY or not dfs(next_node):
                    return False
            color[node] = BLACK
            return True

        return [i for i in range(len(graph)) if dfs(i)]
