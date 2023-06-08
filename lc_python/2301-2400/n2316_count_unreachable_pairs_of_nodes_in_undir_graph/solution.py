class Solution:
    def count_pairs(self, n: int, edges: list[list[int]]) -> int:
        union = [-1] * n
        comp = dict()
        for u, v in edges:
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
        return sum((n - k) * k for k in [len(sub) + 1 for sub in comp.values()] + [1 for u in union if u == -1])//2
