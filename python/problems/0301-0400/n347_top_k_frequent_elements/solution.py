from typing import List, Optional
from collections import Counter, OrderedDict
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(itemgetter(0), sorted(list(dict(Counter(nums)).items()), key=itemgetter(1), reverse=True)[:k]))
        
