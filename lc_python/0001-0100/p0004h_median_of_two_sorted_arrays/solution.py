from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        p1 = 0
        p2 = 0
        mid = 0
        prev_mid = 0
        for _ in range((m + n) // 2 + 1):
            if p2 < n and (p1 >= m or nums1[p1] > nums2[p2]):
                mid, prev_mid = nums2[p2], mid
                p2 += 1
            else:
                mid, prev_mid = nums1[p1], mid
                p1 +=1
            
        if (m + n) % 2 == 0:
            return (mid + prev_mid) / 2
        return mid
