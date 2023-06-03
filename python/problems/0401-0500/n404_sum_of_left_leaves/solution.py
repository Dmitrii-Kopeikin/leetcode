from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_of_left = 0
        if root.left and not root.left.left and not root.left.right:
            sum_of_left += root.left.val
        elif root.left:
            sum_of_left += self.sumOfLeftLeaves(root.left)
        if root.right:
            sum_of_left += self.sumOfLeftLeaves(root.right)
        return sum_of_left