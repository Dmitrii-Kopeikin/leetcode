from typing import List, Optional


class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = writer = 0
        while left < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            for s in chars[left] + (str(right - left) if right - left > 1 else ''):
                chars[writer] = s
                writer += 1
            left = right
            right += 1

        while len(chars) > writer:
            chars.pop()

        return len(chars)