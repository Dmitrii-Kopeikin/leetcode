import bisect
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = []

        lis = []  # lowest increasing sequences

        for i, height in enumerate(obstacles):
            idx = bisect.bisect_right(lis, height)
            print(idx)

            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height

            print(lis)    
            
            result.append(idx + 1)

        return result
    

# Slow
# class Solution:
#     def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
#         result = []
        
#         dp = [-1] * len(obstacles)

#         for i in range(0, len(obstacles)):
#             if i == 0:
#                 dp[i] = 1
#             else:
#                 prev_max_len = 0
#                 for j in range(i - 1, -1, -1):
#                     if dp[j] > prev_max_len and obstacles[j] <= obstacles[i]:
#                         prev_max_len = dp[j]

#                 dp[i] = prev_max_len + 1
#             result.append(dp[i])

#         return result
