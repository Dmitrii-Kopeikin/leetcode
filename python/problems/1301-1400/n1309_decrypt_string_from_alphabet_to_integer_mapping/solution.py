import string

from typing import List


class Solution:
    def freqAlphabets(self, s: str) -> str:
        left, right = 0, 0
        result = ""
        while left < len(s) and right < len(s):
            if right < len(s) - 1 and s[right] != "#":
                right += 1
            elif s[right] == "#" and right - left == 2:
                index = int(s[left:right])
                result += string.ascii_lowercase[index - 1]
                right += 1
                left = right
            else:
                index = int(s[left])
                result += string.ascii_lowercase[index - 1]
                left += 1

        return result
