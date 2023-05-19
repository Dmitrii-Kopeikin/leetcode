from typing import List, Optional


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        (a, b) = zip(*edges)
        return list(set(a).difference(set(b)))
