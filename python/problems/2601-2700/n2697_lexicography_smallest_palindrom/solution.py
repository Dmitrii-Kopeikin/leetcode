from typing import List


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        result_list = [''] * len(s)
        while left <= right:
            next_char = min(s[left], s[right])
            result_list[left] = next_char
            result_list[right] = next_char

            left += 1
            right -= 1

        return "".join(map(str, result_list))