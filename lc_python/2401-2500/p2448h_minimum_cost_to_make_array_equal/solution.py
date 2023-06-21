from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def calc_cost(base):
            return sum([abs(base - num) * cost for num, cost in zip(nums, cost)])
        

        left, right = min(nums), max(nums)
        answer = calc_cost(nums[0])

        while left < right:
            mid = (left + right) // 2
            cost_1 = calc_cost(mid)
            cost_2 = calc_cost(mid + 1)
            answer = min(cost_1, cost_2)

            if cost_1 > cost_2:
                left = mid + 1
            else:
                right = mid

        return answer
