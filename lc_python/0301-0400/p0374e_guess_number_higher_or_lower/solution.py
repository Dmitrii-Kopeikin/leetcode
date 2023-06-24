from typing import List, Optional


def guess(x): return x


class Solution:

    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            res = guess(mid)
            if res == 0:
                return mid
            if res == -1:
                high = mid
            else:
                low = mid + 1

        return -1
