from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}{(' -> ' + str(self.next.val)) if self.next else ''}"


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None:
            raise ValueError

        stack = [head]
        while head.next:
            head = head.next
            stack.append(head)

        max_sum = 0
        n = len(stack)
        for i in range(0, int(n / 2)):
            max_sum = max(max_sum, stack[i].val + stack.pop().val)

        return max_sum
