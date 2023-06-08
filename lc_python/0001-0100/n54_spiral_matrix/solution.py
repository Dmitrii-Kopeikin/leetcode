from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) > 0:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return result
    