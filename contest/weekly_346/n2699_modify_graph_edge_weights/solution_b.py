from typing import List
from collections import defaultdict
from heapq import he


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def create_graph(edges: list[list[int]]) -> dict:
            graph = defaultdict(lambda: defaultdict(dict))

            for source, destination, weight in edges:
                graph[source][destination] = weight
                graph[destination][source] = weight

            return graph

        graph = create_graph(edges)

        if source not in graph or destination not in graph:
            return []

        def filter_paths(path_vars: list):

            min_path = []

            min_weight = target + 1
            for path in path_vars:
                changable_count = 0
                weights_sum = 0
                edges_count = 0
                for start, end, weight in path:
                    edges_count += 1
                    if weight == -1:
                        changable_count += 1
                    else:
                        weights_sum += weight

                if changable_count == 0 and weights_sum < target:
                    return []

                if weights_sum + changable_count > target:
                    continue

                if weights_sum + changable_count < min_weight:
                    min_weight = weights_sum + changable_count
                    min_path = path

            return min_path

        def get_modified_nodes(path_vars: list) -> list:
            modified_nodes = {}
            for path in path_vars:
                path_weight = 0
                changable_count = 0
                for s, e, w in path:
                    if w == -1:
                        modified_nodes[{s, e}] = 1
                        changable_count += 1
                    else:
                        path_weight += w
                

            

        def modify_path(path: list):
            weight = sum([edge[2] for edge in path if edge[2] != -1])
            negatives_count = sum(1 for edge in path if edge[2] == -1)

            if negatives_count == 0:
                return path

            delta = target - weight
            new_weight, reminder = delta // negatives_count, delta % negatives_count
            for i, edge in enumerate(path):
                if negatives_count > 0 and edge[2] == -1:
                    edge[2] = new_weight if negatives_count > 1 else (
                        new_weight + reminder)
                    negatives_count -= 1

            return path

        path_vars = []

        def find_path_vars(start: int, end: int, visited: set[int], path: list):
            if start in visited:
                return

            if start == end:
                path_vars.append(path)
                return

            visited.add(start)
            for next_node, weight in graph[start].items():
                n_path = path.copy()
                n_path.append([start, next_node, weight])
                find_path_vars(next_node, end, set(visited), n_path)

        find_path_vars(source, destination, set(), [])
        print(path_vars)
        path = modify_path(filter_paths(path_vars))
        # print(path)

        weigths_sum = 0
        for i, (s, e, w) in enumerate(edges):
            for s_p, e_p, w_p in path:
                if s_p in (s, e) and e_p in (s, e):
                    edges[i][2] = w_p
                    weigths_sum += edges[i][2]
            if edges[i][2] == -1:
                edges[i][2] = target + 1

        print(source, destination)
        print(edges)

        return edges if weigths_sum == target else []
