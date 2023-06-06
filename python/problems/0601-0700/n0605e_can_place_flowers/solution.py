from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, is_planted in enumerate(flowerbed):
            if is_planted:
                continue
            if not any(flowerbed[max(i - 1, 0): i + 2]):
                flowerbed[i] = 1
                n -= 1
            print (flowerbed)
        return n <= 0
