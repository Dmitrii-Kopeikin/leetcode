from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {str(self.next) if self.next else 'end'}"


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        node = head
        prev_node = None
        stack = []
        while node:
            if len(stack) < k:
                stack.append(node)
                node = node.next
            if len(stack) == k:
                group_node = stack.pop()
                if prev_node is not None:
                    prev_node.next = group_node
                else:
                    head = group_node

                while stack:
                    group_next_node = stack.pop()
                    group_node.next = group_next_node
                    group_node   = group_next_node
                group_node.next = node
                
                prev_node = group_node

        return head
