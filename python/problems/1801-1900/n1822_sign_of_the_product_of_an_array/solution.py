from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            if num == 0:
                return 0
            prod *= num
        
        return int(prod > 0) or -1