from typing import List
from collections import Counter, defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = -1
        comp = defaultdict(int)
        for num, count in Counter(nums).items():
            comp[num] = count * num
            max_num = max(num, max_num)
        memo = {}

        def dp(num: int):
            if num < 0:
                return 0

            if num not in memo:
                memo[num] = max(dp(num - 2) + comp[num], dp(num - 1))

            return memo[num]

        return dp(max_num)
