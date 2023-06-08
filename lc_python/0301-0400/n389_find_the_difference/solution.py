from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        for l in t:
            if l in s_list:
                s_list[s_list.index(l)] = ''
            else:
                return l
