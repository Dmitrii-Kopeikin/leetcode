from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, prices[0]
        
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)

        return max_profit
