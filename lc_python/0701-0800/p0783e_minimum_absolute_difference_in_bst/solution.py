from math import inf
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_distance = inf
        prev_node = None
       
        def traverse(node: TreeNode):
            if node is None:
                return 
            
            traverse(node.left)

            nonlocal prev_node
            nonlocal min_distance
            if prev_node is not None:
                min_distance = min(min_distance, node.val - prev_node.val)
            
            prev_node = node
            traverse(node.right)

        traverse(root)
        return min_distance
