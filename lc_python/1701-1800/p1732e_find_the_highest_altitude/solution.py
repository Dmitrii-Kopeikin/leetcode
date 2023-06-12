from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current = 0
        for net_gain in gain:
            current += net_gain
            highest_altitude = max(highest_altitude, current)
        return highest_altitude
