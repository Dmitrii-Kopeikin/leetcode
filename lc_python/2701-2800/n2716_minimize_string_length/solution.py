from typing import List


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # if len(s) < 1:
        #     return 0
        # answer = 1
        # idx = 1
        # while idx < len(s):
        #     if s[idx] != s[idx - 1]:
        #         answer += 1
        #     idx += 1
        
        # return answer
        return len(set(s))