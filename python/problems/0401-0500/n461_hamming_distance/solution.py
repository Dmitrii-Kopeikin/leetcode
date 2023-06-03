from functools import reduce


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return f"{x ^ y:b}".count('1')