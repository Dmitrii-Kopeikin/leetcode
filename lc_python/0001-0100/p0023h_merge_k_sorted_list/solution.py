from typing import List, Optional
from math import inf

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}{(' -> ' + str(self.next)) if self.next else ''}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:       
        result = head = ListNode(0)

        while result:
            min_node, idx = None, -1
            min_value = inf
            for i, node in enumerate(lists):
                if node and node.val < min_value:
                        min_node = node
                        min_value = node.val
                        idx = i
            if min_node:
                lists[idx] = lists[idx].next
            result.next = min_node
            result = result.next

        return head.next
