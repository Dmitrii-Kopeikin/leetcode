from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        counter = 0
        while node:
            counter += 1
            node = node.next
        for i in range(counter // 2):
            head = head.next
        return head