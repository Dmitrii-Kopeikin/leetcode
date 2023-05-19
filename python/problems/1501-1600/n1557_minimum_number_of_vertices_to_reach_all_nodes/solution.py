from typing import List, Optional


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set()
        for a, _ in edges:
            result.add(a)
        for _, b in edges:
            result.discard(b)
        return list(result)
