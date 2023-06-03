from typing import List


class NumArray:

    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     if left <= right and right < len(self.nums):
    #         return sum(self.nums[left:right + 1])

    #     return None

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for value in nums:
            self.sums.append(self.sums[-1] + value)

    def sumRange(self, left: int, right: int) -> int:
        if left >= 0 and left <= right and right < len(self.sums):
            return self.sums[right + 1] - self.sums[left]

        return None
