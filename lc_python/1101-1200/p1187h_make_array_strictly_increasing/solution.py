from typing import List
from bisect import bisect_right
from math import inf, isinf

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        memo = {}
        
        def dp(idx: int, prev: int):
            if idx >= len(arr1):
                return 0
            if (idx, prev) in memo:
                return memo[(idx, prev)]
            
            cost = inf

            if arr1[idx] > prev:
                cost = dp(idx + 1, arr1[idx])

            idx2 = bisect_right(arr2, prev)
            if idx2 < len(arr2):
                cost = min(cost, 1 + dp(idx + 1, arr2[idx2]))

            memo[(idx, prev)] = cost
            return cost

        result = dp(0, -1)
        return -1 if isinf(result) else result
