from typing import List
from collections import defaultdict


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sum_of_two = sum(prices[:2])
        return (money - sum_of_two) if money >= sum_of_two else money 