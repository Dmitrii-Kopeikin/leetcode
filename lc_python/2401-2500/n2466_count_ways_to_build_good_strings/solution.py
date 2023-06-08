from typing import List


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * (high)
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            
        result = 0
        for i in range(low, high + 1):
            result += dp[i]

        return result % 1_000_000_007
    

class SolutionRecursion:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [-1] * high

        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            result = 0
            if end >= zero:
                result += dfs(end - zero)
            if end >= one:
                result += dfs(end - one)
            dp[end] = result
            return result
        
        result = 0
        for i in range(low, high + 1):
            result += dfs(i)

        return result % 1_000_000_007 