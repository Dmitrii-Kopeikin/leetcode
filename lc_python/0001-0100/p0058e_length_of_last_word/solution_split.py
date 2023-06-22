class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if s else 0
