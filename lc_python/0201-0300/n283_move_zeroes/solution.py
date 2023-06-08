from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        w = 0
        r = 0
        while r < len(nums):
            if nums[r] == 0:
                r += 1
            else:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
        
