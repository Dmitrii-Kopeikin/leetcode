from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            while result and result[-1] > 0 and result[-1] < abs(asteroid) and asteroid < 0:
                result.pop()
            if result and asteroid < 0:
                if result[-1] == abs(asteroid):
                    result.pop()
                elif result[-1] < 0:
                    result.append(asteroid)
            else:
                result.append(asteroid)

        return result
