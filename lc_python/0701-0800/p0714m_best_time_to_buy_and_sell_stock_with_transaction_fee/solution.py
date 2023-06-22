from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, free = -prices[0], 0

        for i in range(1, len(prices)):
            # prev_hold = hold
            # hold = max(hold, free - prices[i])
            # free = max(free, prev_hold + prices[i] - fee)
            hold, free = max(hold, free - prices[i]), max(free, hold + prices[i] - fee)

        return free
