from typing import List
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        snt = list(senate)
        banned_r = 0
        banned_d = 0
        while True:
            for i, s in enumerate(snt):
                if s == 'b':
                    continue
                if s == "R":
                    if banned_r > 0:
                        snt[i] = 'b'
                        banned_r -= 1
                    else:
                        banned_d += 1
                else:
                    if banned_d > 0:
                        snt[i] = 'b'
                        banned_d -= 1
                    else:
                        banned_r += 1
            print(snt)
            if 'R' not in snt:
                return "Dire"
            elif 'D' not in snt:
                return "Radiant"