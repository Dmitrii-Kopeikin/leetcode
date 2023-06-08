from typing import List, Optional


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        if m == 0:
            return True
        if m > n:
            return False

        s_pointer = t_pointer = 0
        while s_pointer < m and t_pointer < n:
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
                if s_pointer >= m:
                    return True
            t_pointer += 1

        return False
