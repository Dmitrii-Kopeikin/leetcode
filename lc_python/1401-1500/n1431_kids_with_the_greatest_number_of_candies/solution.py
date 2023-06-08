from typing import List, Optional


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_count = max(candies)
        return [count + extraCandies >= max_count for count in candies]
