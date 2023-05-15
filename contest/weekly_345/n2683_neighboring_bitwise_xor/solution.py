from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original_v1 = [0] + [0] * len(derived)
        original_v2 = [1] + [0] * len(derived)
        
        for i, b in enumerate(derived):
            original_v1[i + 1] = original_v1[i] ^ b
            original_v2[i + 1] = original_v2[i] ^ b
            
        if original_v1[0] == original_v1[-1] or original_v2[0] == original_v2[-1]:
            return True
        return False