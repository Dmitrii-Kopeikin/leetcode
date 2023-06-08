from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return []

        l_dir_prods = [1] * len(nums)
        r_dir_prods = [1] * len(nums)
        l_dir_prods[0] = nums[0]
        r_dir_prods[-1] = nums[-1]
        l = 1
        r = len(nums) - 2

        while l < len(nums) - 1:
            l_dir_prods[l] = l_dir_prods[l - 1] * nums[l]
            r_dir_prods[r] = r_dir_prods[r + 1] * nums[r]
            if r <= l:
                nums[l] = l_dir_prods[l - 1] * r_dir_prods[l + 1]
                nums[r] = l_dir_prods[r - 1] * r_dir_prods[r + 1]
            l += 1
            r -= 1
        
        nums[0] = r_dir_prods[1]
        nums[-1] = l_dir_prods[-2]

        return nums