from typing import List, Optional

from .solution import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        if not lists and len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        middle = len(lists) // 2
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])

        return self.merge_two_lists(left, right)
    
    def merge_two_lists(self, l1: ListNode, l2:ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 if l1 else l2

        return dummy.next