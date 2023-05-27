from typing import List, Optional


class Solution:
    # Bottom-up dynamic programming
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        m = 4  # len(dp)
        dp = [0] * m

        for i in range(n - 1, -1, -1):
            dp[i % m] = stoneValue[i] - dp[(i + 1) % m]
            if i + 2 <= n:
                dp[i % m] = max(dp[i % m], sum(stoneValue[i:i+2]) - dp[(i + 2) % m])
            if i + 3 <= n:
                dp[i % m] = max(dp[i % m], sum(stoneValue[i:i+3]) - dp[(i + 3) % m])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"

    # Top-down dynamic programming (memoization)
    # def stoneGameIII(self, stoneValue: List[int]) -> str:
    #     n = len(stoneValue)
    #     max_value = 1_000_000_000
    #     dp = [max_value] * (n + 1)
        
    #     def f(i):
    #         if i == n:
    #             return 0
    #         if dp[i] != max_value:
    #             return dp[i]

    #         # return max([(sum(stoneValue[i:j]) - f(j)) for j in range(i + 1, i + 4) if j <= n])

    #         dp[i] = stoneValue[i] - f(i + 1)
    #         j = i + 2
    #         while j <= n and j <= i + 3:
    #             dp[i] = max(dp[i], sum(stoneValue[i:j]) - f(j))
    #             j += 1

    #         return dp[i]

    #     dif = f(0)

    #     if dif > 0:
    #         return "Alice"
    #     if dif < 0:
    #         return "Bob"
    #     return "Tie"
