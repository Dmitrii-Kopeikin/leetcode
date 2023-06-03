from typing import List, Optional
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = deque([0])
        visited = {0}
        while queue:
            room = queue.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.appendleft(key)

        return len(visited) == n
