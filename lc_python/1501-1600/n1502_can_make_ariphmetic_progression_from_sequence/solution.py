from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr or len(arr) < 2:
            return False
        
        if len(arr) == 2:
            return True

        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(len(arr) - 1):
            if arr[i] - arr[i + 1] != diff:
                return False
        
        return True
