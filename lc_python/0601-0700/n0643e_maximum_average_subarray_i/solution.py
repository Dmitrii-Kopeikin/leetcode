from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = sum(nums[0:k])
        current = k_sum
        for i in range(len(nums) - k):
            current = current + nums[i+k] - nums[i]
            k_sum = max(k_sum, current)
        return k_sum / k
