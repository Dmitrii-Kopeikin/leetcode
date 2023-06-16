from typing import List
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1_000_000_007

        def dfs(nums):
            m = len(nums)

            if m < 3:
                return 1

            left_nodes, right_nodes = [], []
            for i in nums:
                if i > nums[0]:
                    right_nodes.append(i)
                elif i < nums[0]:
                    left_nodes.append(i)

            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod

        return dfs(nums) - 1
