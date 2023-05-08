from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            greater_dict[nums2[i]] = stack[-1] if len(stack) else -1
            stack.append(nums2[i])
        
        return [greater_dict[x] for x in nums1]

