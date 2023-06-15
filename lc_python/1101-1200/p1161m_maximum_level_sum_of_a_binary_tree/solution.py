from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level, next_level = deque([root]), deque()
        cur_sum, max_sum = 0, root.val
        cur_level = max_level = 1
        while level:
            node = level.pop()
            cur_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not level:
                if cur_sum > max_sum:
                    max_sum, max_level = cur_sum, cur_level
                level, next_level = next_level, level
                cur_sum = 0
                cur_level += 1

        return max_level
