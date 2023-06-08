from typing import List, Optional


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [1] + [0] * (n)
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])
