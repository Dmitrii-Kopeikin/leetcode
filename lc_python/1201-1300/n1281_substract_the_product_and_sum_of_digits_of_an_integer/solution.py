from typing import List
from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d)for d in str(n)]
        return reduce(lambda p, x: p * x, digits, 1) - sum(digits)
