from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = -1
        min_index = -1
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(point[0] - x) + abs(point[1] - y)
                if min_dist == - 1 or dist < min_dist:
                    min_dist = dist
                    min_index = i
        
        return min_index
        
