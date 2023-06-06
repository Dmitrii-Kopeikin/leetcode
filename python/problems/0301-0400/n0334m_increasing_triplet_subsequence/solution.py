from typing import List
from bisect import bisect_left


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        lis = []
        for i, number in enumerate(nums):
            idx = bisect_left(lis, number)
            if idx >= len(lis):
                lis.append(number)
            else:
                lis[idx] = number
            
        return len(lis) >= 3
