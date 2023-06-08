from typing import List, Optional
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        answer = []
        queue = deque()

        l, r = 0, 0

        while r < len(nums):
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])
            if r - l + 1 == k:
                answer.append(queue[0])
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1
            r += 1

        return answer
