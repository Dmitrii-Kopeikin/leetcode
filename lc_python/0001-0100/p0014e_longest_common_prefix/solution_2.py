from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        prefix = ''
        first_str, second_str = strs[0], strs[-1]
        for i in range(len(first_str)):
            if first_str[i] == second_str[i]:
                prefix += first_str[i]
            else:
                break

        return prefix
