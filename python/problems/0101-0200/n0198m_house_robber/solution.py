from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1] * len(nums)

        def rob_next(house: int) -> int:
            if house >= len(nums):
                return 0
            
            if memo[house] == -1:
                memo[house] = nums[house] + max(rob_next(house + 2), rob_next(house + 3))

            return memo[house]

        return max(rob_next(0), rob_next(1))
