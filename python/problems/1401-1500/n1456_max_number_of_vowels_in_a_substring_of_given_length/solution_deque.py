from collections import deque
from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        substring = deque(maxlen=k)
        vowels_count = 0
        vowels_max = 0
        for i, letter in enumerate(s):
            if i >= k:
                out_letter = substring.popleft()
                if out_letter in vowels:
                    vowels_count -= 1
            substring.append(letter)
            if letter in vowels:
                vowels_count += 1
            if vowels_count > vowels_max:
                vowels_max = vowels_count

        return vowels_max
