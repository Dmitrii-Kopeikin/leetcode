from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [i for i in range(n ** 2)]

        matrix = []
        


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) > 0:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return result
    