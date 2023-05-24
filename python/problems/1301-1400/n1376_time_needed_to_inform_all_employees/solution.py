from typing import List, Optional
from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(id: int):
            if manager[id] != -1:
                informTime[id] += dfs(manager[id])
            return informTime[id]

        return max(dfs(i) for i in range(n) if informTime[i] == 0)

