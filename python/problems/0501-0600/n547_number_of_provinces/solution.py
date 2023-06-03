from typing import List, Optional
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected[0])

        groups_count = 0
        for i in range(n):
            queue = deque([i])
            has_connections = False
            while queue:
                row = queue.pop()
                for idx, value in enumerate(isConnected[row]):
                    if value == 1:
                        queue.appendleft(idx)
                        isConnected[row][idx] = -1
                        has_connections = True

            groups_count += int(has_connections)

        return groups_count
