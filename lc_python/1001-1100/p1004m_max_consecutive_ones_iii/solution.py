from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return len(nums) - left

        left = right = 0
        max_len = 0
        zeros_count = 0
        while right < len(nums):
            while right < len(nums) and (nums[right] != 0 or zeros_count < k):
                if nums[right] == 0:
                    zeros_count += 1
                right += 1
            max_len = max(max_len, right - left)
            while right < len(nums) and zeros_count >= k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

        return max_len
