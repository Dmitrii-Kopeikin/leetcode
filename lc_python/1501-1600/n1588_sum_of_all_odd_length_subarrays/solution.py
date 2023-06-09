from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(0, len(arr) + 1 - i):
                result += sum(arr[j:j + i])
                j += 1
        
        return result
