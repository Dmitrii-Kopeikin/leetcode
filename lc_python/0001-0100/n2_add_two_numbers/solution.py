from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = f"{self.val}"
        next_node = self.next
        while next_node:
            result += str(next_node.val)
            next_node = next_node.next
        return result


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        next = result
        while l1 or l2:
            l1_val = l2_val = 0
            if l1:
                l1_val, l1 = l1.val, l1.next
            if l2:
                l2_val, l2 = l2.val, l2.next
            summ = l1_val + l2_val + next.val
            next.val = summ % 10
            if l1 or l2 or summ >= 10:
                next.next = ListNode(summ // 10)
            next = next.next

        return result
