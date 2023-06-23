from typing import List, Optional
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        answer = 2
        num_range = max(nums) - min(nums)

        for abs_diff in range(num_range + 1):
            if abs_diff * (answer - 1) >= num_range:
                break
            for diff in (-abs_diff, abs_diff):
                counter = defaultdict(lambda: 1)
                for num in nums:
                    prev_num = num - diff
                    if prev_num in counter:
                        counter[num] = max(counter[num], counter[prev_num] + 1)
                    answer = max(answer, counter[num])

        return answer
