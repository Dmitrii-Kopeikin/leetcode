from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                result += 1 << (j - i)
                i += 1
            else:
                j -= 1
        
        return result % (10 ** 9 + 7)
