from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        left_index = 0
        right_index = len(nums) - 1
        for i, num in enumerate(nums):
            if num == 1:
                left_index = i
            if num == len(nums):
                right_index = i
        
        answer = left_index + (len(nums) - 1 - right_index)
        if left_index > right_index:
            answer -= 1

        return answer