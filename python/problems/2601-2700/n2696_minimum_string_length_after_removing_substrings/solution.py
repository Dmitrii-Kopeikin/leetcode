from typing import List


class Solution:
    def minLength(self, s: str) -> int:
        s_list = list(s)
        i = 0
        pairs = {"A": "B", "C": "D"}
        while i < len(s_list) - 1:
            if s_list[i] in pairs and s_list[i + 1] == pairs[s_list[i]]:
                del s_list[i:i + 2]
                i = max(0, i - 1)
            else:
                i += 1

        return len(s_list)