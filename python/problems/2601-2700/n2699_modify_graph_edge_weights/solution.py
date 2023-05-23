from typing import List
from collections import defaultdict


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
        
        def check_paths(path_vars: list):
            if not path_vars:
                return []

            print(path_vars)
            short_path_vars = []
            for path in path_vars:
                weights_sum = 0
                changable_count = 0
                for s, e, weight in path:
                    if weight != -1:
                        weights_sum += weight
                    else:
                        changable_count += 1
                if weights_sum + changable_count <= target:
                    short_path_vars.append([path, changable_count])

            print(short_path_vars)
            if len(short_path_vars) == 1 and short_path_vars[0][1] != 0:
                return short_path_vars[0][0]
                
            return []
        
        def modify_path(path: list):
            weight = sum([edge[2] for edge in path if edge[2] != -1])
            negatives_count = sum(1 for edge in path if edge[2] == -1)

            if negatives_count == 0:
                return path

            delta = target - weight
            new_weight, reminder = delta // negatives_count, delta % negatives_count
            for i, edge in enumerate(path):
                if negatives_count > 0 and edge[2] == -1:
                    edge[2] = new_weight if negatives_count > 1 else (new_weight + reminder)
                    negatives_count -= 1
            
            return path

        def find_path_vars(start: int, end: int, visited: set[int]) -> list:
            if start in visited:
                return []

            visited.add(start)
            path_vars = []
            for next_node, weight in graph[start].items():
                if next_node == end:
                    path_vars.append([start, next_node, weight])
                else:
                    next_path_vars = find_path_vars(next_node, end, set(visited))
                    if next_path_vars:
                        for path_var in path_vars:
                            path_vars.append([[start, next_node, weight]] + next_path_vars)

            return path_vars

        path_vars = find_path_vars(source, destination, set())
        print(source, destination)
        print(path_vars)

        return []
        # path = modify_path(path)
        # print(path)

        # weigths_sum = 0
        # for i, (s, e, w) in enumerate(edges):
        #     for s_p, e_p, w_p in path:
        #         if s_p in (s, e) and e_p in (s, e):
        #             edges[i][2] = w_p
        #             weigths_sum += edges[i][2]
        #     if edges[i][2] == -1:
        #         edges[i][2] = target + 1

        # return edges if weigths_sum == target else []