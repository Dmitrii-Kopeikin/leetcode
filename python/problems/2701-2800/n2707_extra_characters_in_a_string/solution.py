from typing import List


class Solution:
    def minExtraChar(self, string: str, dictionary: List[str]) -> int:
        cache = {}

        def dp(i: int, extra: int) -> int:
            if i >= len(string):
                return extra

            if (i + 1, extra) not in cache:
                cache[(i + 1, extra)] = dp(i + 1, extra)
            min_extra = cache[(i + 1, extra)]

            for word in dictionary:
                if string[i:].startswith(word):
                    if (i + len(word), extra - len(word)) not in cache:
                        cache[(i + len(word), extra - len(word))] = dp(i + len(word), extra - len(word))
                    min_extra = min(
                        min_extra,
                        cache[(i + len(word), extra - len(word))],
                    )

            return min_extra

        return dp(0, len(string))