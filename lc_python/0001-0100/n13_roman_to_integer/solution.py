from typing import List


class Solution:

    def __init__(self):
        self.values_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }


    def romanToInt(self, s: str) -> int:
        
        result = 0
        prev = 0
        for c in s:
            value = self.values_map[c]
            if (((value == 5 or value == 10) and prev == 1)
            or ((value == 50 or value == 100) and prev == 10)
            or ((value == 500 or value == 1000) and prev == 100)):
                value -= prev * 2
            result += value
            prev = value

        return result
    