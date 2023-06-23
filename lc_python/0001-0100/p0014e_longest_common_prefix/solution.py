from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        i = 0
        while i < min(list(map(len, strs))):
            l = strs[0][i]
            prefix.append(l)
            for s in strs:
                if s[i] != l:
                    prefix.pop()
                    return ''.join(prefix)
            i += 1
        return ''.join(prefix)
