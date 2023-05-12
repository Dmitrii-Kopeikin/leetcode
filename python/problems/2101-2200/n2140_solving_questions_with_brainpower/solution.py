from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}

        def solve(i: int):
            if i >= len(questions):
                return 0
            
            if i in memo:
                return memo[i]

            if i == len(questions) - 1:
                memo[i] = questions[i][0]
            else:
                memo[i] = max(questions[i][0] + solve(1 + i + questions[i][1]), solve(i + 1))

            return memo[i]
        
        return solve(0)