from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat) // 2):
            j = - i - 1
            result += mat[i][i] + mat[i][j] + mat[j][i] + mat[j][j]
        if len(mat) % 2 != 0:
            result += mat[len(mat) // 2][len(mat) // 2]
        return result
    