class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.capacity = 1000
        self.buckets = [None] * self.capacity

    def _calculate_idx(self, key: int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        idx = self._calculate_idx(key)
        
        if self.buckets[idx] is None:
            node = ListNode(val=key)
            self.buckets[idx] = node
            return
        
        node = self.buckets[idx]
        while node:
            if node.val == key:
                return
            if node.next is None:
                node.next = ListNode(val=key)        
                return 
            node = node.next


    def remove(self, key: int) -> None:
        idx = self._calculate_idx(key)
        head = self.buckets[idx]
        prev = None
        node: ListNode = head
        while node:
            if node.val == key:
                if prev:
                    prev.next = node.next
                if node is head:
                    self.buckets[idx] = node.next
            node = node.next

    def contains(self, key: int) -> bool:
        idx = self._calculate_idx(key)
        node: ListNode = self.buckets[idx]
        while node:
            if node.val == key:
                return True
            
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
