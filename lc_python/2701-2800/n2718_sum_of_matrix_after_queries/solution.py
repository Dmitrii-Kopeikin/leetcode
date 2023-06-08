from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        answer = 0
        cache = [set(), set()]

        for type, index, value in queries[::-1]:
            if index in cache[type]:
                continue
            answer += value * (n - len(cache[type - 1]))
            cache[type].add(index)
            if sum(map(len, cache)) >= 2 * n:
                break

        return answer
