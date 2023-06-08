from typing import List
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if not bombs:
            return 0

        def get_distance(x: int, y: int, o_x: int, o_y: int) -> float:
            distance = sqrt((x - o_x) ** 2 + (y - o_y) ** 2)
            return distance

        def can_bomb_detonate(bomb: list, other_bomb: list) -> bool:
            distance = get_distance(bomb[0], bomb[1], other_bomb[0], other_bomb[1])
            return bomb[2] >= distance

        def dfs(bomb: list, visited: set = None) -> int:
            if visited is None:
                visited = set()

            bombs_detonated = 1
            visited.add(bomb[3])

            for i, next_bomb in enumerate(bombs):
                if i in visited:
                    continue
                if can_bomb_detonate(bomb, next_bomb):
                    new_bombs_detonated = dfs(next_bomb + [i], visited)
                    bombs_detonated += new_bombs_detonated

            return bombs_detonated

        return max([dfs(bomb + [i]) for i, bomb in enumerate(bombs)])