from typing import List, Optional


class Solution:
    # def countBits(self, n: int) -> List[int]:
    #     answer = []
    #     for i in range(n + 1):
    #         answer.append(bin(i).count('1'))
        # return answer
    
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i//2] + i % 2
        return result
