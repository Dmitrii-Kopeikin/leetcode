from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        freq = 0
        for i in range(len(arr)):
            freq = freq - (i + 1) // 2 + (len(arr) - i + 1) // 2
            result += freq * arr[i]
        
        return result
