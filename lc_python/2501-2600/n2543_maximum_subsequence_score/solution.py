from typing import List, Optional
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        indices = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        nums1 = [nums1[i] for i in indices]
        nums2 = [nums2[i] for i in indices]

        k_heap = nums1[:k]
        k_sum = sum(k_heap)
        heapq.heapify(k_heap)

        max_score = k_sum * nums2[k - 1]

        for i in range(k, len(nums1)):
            k_sum += nums1[i] - heapq.heappop(k_heap)
            heapq.heappush(k_heap, nums1[i])

            max_score = max(max_score, k_sum * nums2[i])

        return max_score
