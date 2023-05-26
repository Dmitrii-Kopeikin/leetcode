from typing import List, Optional
from collections import defaultdict


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        memo = defaultdict(int)

        def f(p, i, m):
            if i == n:
                return 0
            res = 1000000 if p == 1 else -1
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if p == 0:
                    req = (1 if p == 0 else 0, i + x, max(m, x))
                    if req not in memo:
                        memo[req] = f(*req)
                    res = max(res, s + memo[req])
                else:
                    req = (0, i + x, max(m, x))
                    if req not in memo:
                        memo[req] = f(*req)
                    res = min(res, memo[req])
            return res
        
        return f(0, 0, 1)
