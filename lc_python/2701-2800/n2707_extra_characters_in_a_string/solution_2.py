from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] + [float('inf')] * len(s)

        for i in range(1, len(dp)):
            for word in dictionary:
                if s[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)])
            dp[i] = min(dp[i], dp[i - 1] + 1)
        return dp[-1]
