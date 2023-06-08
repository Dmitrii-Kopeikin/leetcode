from typing import List, Optional


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(start: int):
            if start < 0 or start >= len(arr) or start in visited:
                return False
            if arr[start] == 0:
                return True
            visited.add(start)
            left = start - arr[start]
            right = start + arr[start]
            return any([dfs(left), dfs(right)])
        
        return dfs(start)
