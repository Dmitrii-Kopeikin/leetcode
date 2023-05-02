from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = -1
        i = len(arr) - 1
        while i >= 0:
            if arr[i] > n:
                n, arr[i] = arr[i], n 
            else:
                arr[i] = n
            i -= 1
        return arr
    