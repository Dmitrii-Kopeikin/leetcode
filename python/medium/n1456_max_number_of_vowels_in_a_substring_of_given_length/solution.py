from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        vowels_max = 0
        vowels_count = 0
        for i, letter in enumerate(s):
            if i >= k:
                if s[i - k] in vowels:
                    vowels_count -= 1
            if letter in vowels:
                vowels_count += 1
            if vowels_count > vowels_max:
                vowels_max = vowels_count

        return vowels_max
