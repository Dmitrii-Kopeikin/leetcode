from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [i for i in range(1, n ** 2 + 1)]

        matrix = [[nums[-1]]]
        start = 1
        while len(matrix) < n:
            arr = nums[-(start + len(matrix[0])):-start]
            matrix.append(arr)
            matrix = list(zip(*matrix))[::-1]
            start += len(arr)
        
        matrix = list(zip(*matrix))[::-1]
        matrix = list(map(lambda x: list(x)[::-1], matrix))
        return matrix


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) > 0:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return result
    