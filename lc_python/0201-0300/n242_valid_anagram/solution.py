import string

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [l for l in s if l in string.ascii_lowercase]
        t_list = [l for l in t if l in string.ascii_lowercase]
        s_list.sort()
        t_list.sort()
        return s_list == t_list
