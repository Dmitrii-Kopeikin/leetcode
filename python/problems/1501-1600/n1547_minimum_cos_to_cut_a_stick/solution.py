from typing import List, Optional


class Solution:

    # Bottom-up dynamic programming
    def minCost(self, n: int, cuts: List[int]) -> int:
        new_cuts = [0] + sorted(cuts) + [n]
        m = len(new_cuts)
        dp = [[0 for _ in range(m)] for _ in range(m)]

        for diff in range(2, m):
            for left in range(m - diff):
                right = left + diff
                answer = float('inf')
                for mid in range(left + 1, right):
                    answer = min(
                        answer,
                        dp[left][mid] + dp[mid][right] +
                        new_cuts[right] - new_cuts[left],
                    )
                dp[left][right] = answer

        return dp[0][m - 1]

    # Top-down dynamic programming
    # def minCost(self, n: int, cuts: List[int]) -> int:
    #     new_cuts = [0] + sorted(cuts) + [n]
    #     dp = [[-1 for _ in range (n + 2)] for _ in range(n + 2)]

    #     def cost(left: int, right: int):
    #         if right - left == 1:
    #             return 0

    #         if dp[left][right] != -1:
    #             return dp[left][right]

    #         answer = min(
    #             cost(left, mid) + cost(mid, right) + new_cuts[right] - new_cuts[left] for mid in range(left + 1, right)
    #         )
    #         dp[left][right] = answer
    #         return answer

    #     return cost(0, len(new_cuts) - 1)
