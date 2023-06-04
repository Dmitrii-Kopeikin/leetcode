from typing import List
from functools import cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        modulo = 1_000_000_007

        @cache
        def ct1(n, m1, m2, min_sum, max_sum):
            if max_sum < 0:
                return 0
            if min_sum < 0:
                min_sum = 0
            if n == 0:
                return sum(1 for it in range(m1, m2) if min_sum <= it <= max_sum)
            ans = 0
            for m in range(m1, m2):
                ans += ct1(n - 1, 0, 10, min_sum - m, max_sum - m)
            return ans % modulo

        def ct0(s, min_sum, max_sum):
            l = len(s)
            ans = 0
            s1 = 0
            for i in range(l):
                ans += ct1(l - 1 - i, 0, int(s[i]), min_sum - s1, max_sum - s1)
                s1 += int(s[i])
            return ans % modulo

        ans = ct0(num2, min_sum, max_sum) - ct0(num1, min_sum, max_sum)
        if min_sum <= sum(int(c) for c in num2) <= max_sum:
            ans += 1
        return ans % modulo
