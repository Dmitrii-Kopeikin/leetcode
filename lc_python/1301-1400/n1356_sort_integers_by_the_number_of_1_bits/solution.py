from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # arr.sort()
        # arr.sort(key=lambda x: f"{x:b}".count("1"))
        # return arr

        arr_p = [(bin(i).count('1'), i) for i in arr]
        arr_p.sort()
        return [item[1] for item in arr_p]