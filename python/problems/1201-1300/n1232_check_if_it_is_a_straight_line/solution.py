from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) < 2:
            return False
        if len(coordinates) == 2:
            return True
        
        a = coordinates[1][1] - coordinates[0][1]
        b = coordinates[0][0] - coordinates[1][0]
        c = coordinates[1][0] * coordinates[0][1] - coordinates[1][1] * coordinates[0][0]
        for i in range(2, len(coordinates)):
            if a * coordinates[i][0] + b * coordinates[i][1] + c != 0:
                return False

        return True
