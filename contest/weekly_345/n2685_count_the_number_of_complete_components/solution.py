from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        union = [-1] * n
        nodes_edges = [0] * n
        comp = dict()
        for u, v in edges:
            nodes_edges[u] += 1
            nodes_edges[v] += 1
            if union[u] >= 0 and union[v] >= 0:
                if union[u] == union[v]:
                    continue
                if len(comp[union[u]]) < len(comp[union[v]]):
                    u, v = v, u
                nodes = comp.pop(union[v]) + [union[v]]
                for vv in nodes:
                    union[vv] = union[u]
                    comp[union[u]].append(vv)
            elif union[u] >= 0:
                union[v] = union[u]
                comp[union[u]].append(v)
            elif union[v] >= 0:
                union[u] = union[v]
                comp[union[v]].append(u)
            else:
                union[v] = v
                union[u] = v
                comp[v] = [u]

        result = 0
        for group, nodes in comp.items():
            is_complete = True
            group = [group] + nodes
            for node in group:
                if nodes_edges[node] < len(group) - 1:
                    is_complete = False
                    break
            if is_complete:
                result += 1

        return result + union.count(-1)