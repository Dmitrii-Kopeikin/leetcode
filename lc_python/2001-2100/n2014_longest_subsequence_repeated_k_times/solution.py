from typing import List, Optional
from collections import Counter, deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        letters = sorted([l for l, c in dict(Counter(s)).items() if c >= k])
        if len(letters) == 0:
            return ''
        
        def is_repeated_k_times(subseq: str, k: int):
            i, count = 0 , 0
            for l in s:
                if subseq[i] == l:
                    i += 1
                    if i == len(subseq):
                        count += 1
                        if count == k:
                            return True
                        i = 0
            return False

        result = ''
        queue = deque([""])
        while queue:
            subseq_prev = queue.popleft()
            for l in letters:
                subseq_next = subseq_prev + l
                if is_repeated_k_times(subseq_next, k):
                    result = subseq_next
                    queue.append(result)

        return result
