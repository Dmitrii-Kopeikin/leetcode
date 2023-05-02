from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        if not nums or len(nums) < 2:
            return []
        
        l = len(nums)
        
        res = [1] * l

        pr = 1
        pst = 1

        for i, j in zip(range(0, l), range(l - 1, -1, -1)):
            res[i] = pr * res[i]
            res[j] = pst * res[j]

            pr *= nums[i]
            pst *= nums[j]

        return res