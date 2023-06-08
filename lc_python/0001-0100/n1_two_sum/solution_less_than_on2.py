from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_dict = {}
        for i, num in enumerate(nums):
            t_dict[target - num] = i
        for i, num in enumerate(nums):
            if num in t_dict and t_dict[num] != i:
                return [i, t_dict[num]]
        return []
    