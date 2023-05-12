from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) < 2:
            return False
        if len(coordinates) == 2:
            return True
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x0 - x1) * (y - y0) != (y0 - y1) * (x - x0):
                return False

        return True