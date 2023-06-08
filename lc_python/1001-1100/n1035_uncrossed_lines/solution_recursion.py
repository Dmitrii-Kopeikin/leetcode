from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        
        if nums1[-1] == nums2[-1]:
            return 1 + self.maxUncrossedLines(nums1[:-1], nums2[:-1])
        else:
            return max(self.maxUncrossedLines(nums1, nums2[:-1]), self.maxUncrossedLines(nums1[:-1], nums2))
