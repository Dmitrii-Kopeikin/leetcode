from typing import List
from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def create_dp(rods_part: List[int]) -> defaultdict:
            dp = defaultdict(int)
            dp[0] = 0

            for rod in rods_part:
                new_dp = dp.copy()
                for diff, taller in dp.items():
                    shorter = taller - diff
                    new_dp[diff+rod] = max(new_dp[diff+rod], taller + rod)
                    new_diff = abs(shorter + rod - taller)
                    new_taller = max(shorter + rod, taller)
                    new_dp[new_diff] = max(new_dp[new_diff], new_taller)
                dp = new_dp

            return dp
        
        left_dp = create_dp(rods[:len(rods)//2])
        right_dp = create_dp(rods[len(rods)//2:])

        # return max([(l_t + right_dp[l_diff] - l_diff) for l_diff, l_t in left_dp.items() if l_diff in right_dp])

        max_height = 0
        for left_diff, left_taller in left_dp.items():
            if left_diff not in right_dp:
                continue
            max_height = max(max_height, left_taller + right_dp[left_diff] - left_diff)

        return max_height

