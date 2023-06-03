from typing import List, Optional
import heapq
from bisect import bisect


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums[len(nums) - k:len(nums)] if len(nums) > k else nums

    def add(self, val: int) -> int:
        self.nums.insert(bisect(self.nums, val), val)
        if len(self.nums) > self.k:
            self.nums = self.nums[1:]
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.heap = nums
#         heapq.heapify(self.heap)

#         while len(self.heap) > k:
#             heapq.heappop(self.heap)


#     def add(self, val: int) -> int:
#         heapq.heappush(self.heap, val)
#         if len(self.heap) > self.k:
#             heapq.heappop(self.heap)
#         return self.heap[0]
