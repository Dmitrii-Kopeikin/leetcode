from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def calc_cost(base: int) -> int:
            return sum([abs(base - num) * cost for num, cost in zip(nums, cost)])
        
        mid = sum(cost) / 2
        count = 0
        for num, c in sorted(zip(nums, cost)):
            count += c
            if count >= mid:
                return calc_cost(num) 
            