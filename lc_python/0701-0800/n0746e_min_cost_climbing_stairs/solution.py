from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        def make_step(stage: int):
            if stage >= n - 2:
                return cost[stage]

            if dp[stage] == -1:
                dp[stage] = cost[stage] + min(make_step(stage + 1), make_step(stage + 2))
            
            return dp[stage]

        return min(make_step(0), make_step(1))
