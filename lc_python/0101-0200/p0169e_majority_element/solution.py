from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > n / 2:
                return num
