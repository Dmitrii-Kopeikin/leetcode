from typing import List, Optional


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        stack = []
        def solve(n, stack: list[int], set_a: set[int] = set(), set_b: set[int] = set()) -> bool:
            stack.append(n)

            if n in set_b:
                return False
            
            set_a.add(n)

            for nn in graph[n]:
                if nn not in set_b and not solve(nn, stack, set_b, set_a):
                    return False
            
            return True

        for n in range(len(graph)):
            if n not in stack and not solve(n, stack):
                    return False

        return True
