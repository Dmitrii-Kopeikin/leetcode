from typing import List, Optional
from collections import defaultdict


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def build_graph() -> dict:
            graph = defaultdict(dict)
            for i, [dividend, divisor] in enumerate(equations):
                graph[dividend][divisor] = values[i]
                graph[divisor][dividend] = 1 / values[i]

            return graph

        def find_path_value(node: str, dest_node: str, path_value: float, visited: set[str]) -> float:
            if node in visited:
                return -1.0

            visited.add(node)
            if node == dest_node:
                return path_value

            for next_node, value in graph[node].items():
                result = find_path_value(next_node, dest_node, path_value * value, visited)
                if result != -1.0:
                    return result
            
            return -1.0

        answer = []
        graph = build_graph()
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                answer.append(-1.0)
            else:
                answer.append(find_path_value(dividend, divisor, 1.0, set()))

        return answer
