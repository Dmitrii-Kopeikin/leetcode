from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                    return True
        return False
