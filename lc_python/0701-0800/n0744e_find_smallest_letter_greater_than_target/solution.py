from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        if letters[left] > target or letters[right] <= target:
            return letters[0]
        
        while left < right:
            mid = left // 2 + right // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return letters[left]