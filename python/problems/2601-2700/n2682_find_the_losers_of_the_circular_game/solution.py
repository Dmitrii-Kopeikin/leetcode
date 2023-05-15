from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        losers = {i for i in range(1, n + 1)}
        next = 1
        m = 0
        while True:
            next = (next + m * k)
            if next > n:
                next %= n
                if next == 0:
                    next = n
            if next not in losers:
                break
            m += 1
            losers.discard(next)
        
        return list(losers)