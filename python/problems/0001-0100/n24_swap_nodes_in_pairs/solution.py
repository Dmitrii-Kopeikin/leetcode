from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next.val if self.next else 'end'}"


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev_node = None
        while node and node.next:
            next_node = node.next
            node.next, next_node.next = next_node.next, node
            if prev_node is None:
                head = next_node
            else:
                prev_node.next = next_node

            prev_node = node
            node = node.next
        return head
