from typing import List


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(idx: int, str_number: str, target: int) -> bool:
            if idx == len(str_number):
                return target == 0
            if target < 0:
                return False
            for i in range(idx, len(str_number)):
                x = str_number[idx:i + 1]
                y = int(x)
                if check(i + 1, str_number, target - y):
                    return True
            return False

        answer = 0
        for i in range(1, n + 1):
            number = i ** 2
            if check(0, str(number), i):
                answer += number

        return answer