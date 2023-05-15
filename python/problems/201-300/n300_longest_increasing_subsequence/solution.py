import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = []

        for i, num in enumerate(nums):
            idx = bisect.bisect_left(lis, num)

            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num

        return len(lis)