from typing import List, Optional


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def find_path_vars(start: int, end: int, path: list, paths: list):
            if start == end:
                paths.append(path)
                return

            for next_node in graph[start]:
                if next_node not in path:
                    find_path_vars(next_node, end, path + [next_node], paths)

        paths = []
        find_path_vars(0, len(graph) - 1, [0], paths)

        return paths
