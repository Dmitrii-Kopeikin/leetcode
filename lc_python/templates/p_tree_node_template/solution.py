from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val}{(' -> ' + str(self.next.val)) if self.next else ''}"


class Solution:
    def some_method(*args):
        return None
