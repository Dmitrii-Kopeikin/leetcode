from typing import List, Optional
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2 or str1 + str2 != str2 + str1:
            return ''
        
        g = gcd(len(str1), len(str2))
        return str1[:g]

