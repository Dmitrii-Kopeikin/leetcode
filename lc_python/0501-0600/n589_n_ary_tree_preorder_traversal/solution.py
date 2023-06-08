from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        prevs = [root]
        while prevs:
            next = prevs.pop() 
            result.append(next.val)
            if next.children:
                prevs += next.children[::-1]

        return result

