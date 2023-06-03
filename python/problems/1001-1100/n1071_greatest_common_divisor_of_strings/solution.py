from typing import List, Optional


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = min(str1, str2, key=len)

        def check_is_divisor(word: str, prefix: str) -> bool:
            coef, rem = divmod(len(word), len(prefix))
            if rem > 0:
                return False
            return prefix * coef == word

        while prefix:
            if not str1.startswith(prefix) or not str2.startswith(prefix):
                return ''
            if check_is_divisor(str1, prefix) and check_is_divisor(str2, prefix):
                return prefix
            prefix = prefix[:-1]

        return prefix



        