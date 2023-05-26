from typing import List, Optional
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        judges = {i + 1 for i in range(n)}
        
        judjes_dict = defaultdict(set)
        for p, t in trust:
            judjes_dict[t].add(p)
            judges.discard(p)

        for judge in judges:
            if len(judjes_dict[judge]) == n - 1:
                return judge 
            
        return -1
            
        # for p, t in trust:
        #     if p in judjes:
        #         judjes.pop(p)

        # for judje, people in judjes.items():
        #     if len(people) == n - 1:
        #         return judje
        
        # return -1
        
