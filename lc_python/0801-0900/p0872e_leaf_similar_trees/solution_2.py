from collections import deque

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node: TreeNode):
            stack = []
            leaves = []
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    node = node.right
            return leaves

        return get_leaves(root1) == get_leaves(root2)
