from typing import List, Optional


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        post = sum(nums)
        pre = 0
        for i in range(len(nums)):
            post -= nums[i]
            if post == pre:
                return i
            pre += nums[i]
            
        return -1
