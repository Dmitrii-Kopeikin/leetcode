class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = 0
        p = len(s) - 1
        while p >= 0 and s[p].isspace():
            p -= 1
        end = p
        while p >= 0 and s[p].isalpha():
            p -= 1

        return end - p
