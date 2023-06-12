from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        start = 0
        for end, num in enumerate(nums):
            if end == len(nums) - 1 or num + 1 != nums[end+1]:
                answer.append(f'{nums[start]}->{num}' if start != end else f'{num}')
                start = end + 1
            
        return answer
