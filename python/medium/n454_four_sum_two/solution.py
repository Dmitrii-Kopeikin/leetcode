from collections import defaultdict
from typing import List
    

class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:           
        hash_map = defaultdict(int)
        result = 0

        for i in nums1:
            for j in nums2:
                hash_map[i + j] += 1
        
        for k in nums3:
            for l in nums4:
                result += hash_map[-(k + l)]

        return result
