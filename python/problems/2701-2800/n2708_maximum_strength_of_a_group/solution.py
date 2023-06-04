from typing import List
from functools import reduce


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        strength = 1
        max_negative = -10
        neg_count = 0
        pos_count = 0
        has_zero = False
        for i in nums:
            if i != 0:
                strength *= i
            if i < 0:
                neg_count += 1
                max_negative = max(max_negative, i)
            elif i > 0:
                pos_count += 1
            else:
                has_zero = True

        if pos_count == 0 and neg_count == 0:
            return 0
        if pos_count == 0 and has_zero and neg_count < 2:
            return 0
        return strength // max_negative if strength < 0 and len(nums) > 1 else strength
            