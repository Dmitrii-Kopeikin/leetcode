from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}{(' ' + str(self.next)) if self.next else ''}"


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        nodes_arr = []
        while node:
            nodes_arr.append(node)
            node = node.next
        
        nodes_arr[k - 1], nodes_arr[-k] = nodes_arr[-k], nodes_arr[k - 1]
        nodes_arr[k - 1].next = nodes_arr[k] if k < len(nodes_arr) else None
        nodes_arr[-k].next = nodes_arr[-(k - 1)] if k > 1 else None

        if k != 1:
            nodes_arr[k - 2].next = nodes_arr[k - 1]
        if k != len(nodes_arr):
            nodes_arr[-k - 1].next = nodes_arr[-k]

        head = nodes_arr[0]

        return head

