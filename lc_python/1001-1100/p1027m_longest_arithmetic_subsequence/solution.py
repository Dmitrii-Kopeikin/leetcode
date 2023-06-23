from typing import List, Optional
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        visited = set()

        for right in nums:
            for left in visited:
                length = right - left
                dp[(right, length)] = dp[(left, length)] + 1
            visited.add(right)

        return max(dp.values())
