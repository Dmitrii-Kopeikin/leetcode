from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1
        cols = {}
        for col in zip(*grid):
            cols[tuple(col)] = cols.get(col, 0) + 1

        pairs = 0
        for row, count in rows.items():
            pairs += count * cols.get(row, 0)

        return pairs
