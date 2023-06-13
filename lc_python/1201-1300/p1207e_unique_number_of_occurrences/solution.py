from typing import List, Optional


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for elem in arr:
            counter[elem] = counter.get(elem, 0) + 1
        
        return len(counter.values()) == len(set(counter.values()))
