from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        new_mat = [[] * c for r in range(r)]
        n_i = 0
        n_j = 0
        for j in range(len(mat)):
            for i in range(len(mat[0])):
                new_mat[n_j].append(mat[j][i])
                n_i += 1
                if n_i == c:
                    n_i = 0
                    n_j += 1
        return new_mat