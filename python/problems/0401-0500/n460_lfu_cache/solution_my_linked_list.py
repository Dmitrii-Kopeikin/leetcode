class LFUCache:

    class Node:

        def __init__(self, key, value, prev_node=None, next_node=None):
            self.prev_node = prev_node
            self.next_node = next_node
            self.key = key
            self.value = value
            self.counter = 1

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_len = 0

        self.start_node = None

    def appendleft(self, key, value):
        node = self.Node(key, value)
        if self.start_node != None:
            node.next_node = self.start_node
            self.start_node.prev_node = node
        self.start_node = node

    def remove(self, node):
        if node.prev_node != None:
            node.prev_node.next_node = None if node.next_node == None else node.next_node
        else:
            self.start_node = node.next_node
        if node.next_node != None:
            node.next_node.prev_node = None if node.prev_node == None else node.prev_node

    def movetostart(self, node):
        if node.prev_node == None:
            return
        node.prev_node.next_node = node.next_node if node.next_node != None else None
        if node.next_node != None:
            node.next_node.prev_node = node.prev_node
        node.prev_node = None
        node.next_node = self.start_node
        self.start_node.prev_node = node
        self.start_node = node

    def get(self, key: int) -> int:
        if self.cache_len == 0:
            return -1

        node = self.start_node
        while node != None:
            if node.key == key:
                node.counter += 1
                self.movetostart(node)
                return node.value
            node = node.next_node

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        node = self.start_node
        lfu_node = self.start_node
        while node != None:
            if node.key == key:
                node.value = value
                node.counter += 1
                self.movetostart(node)
                return
            if node.counter <= lfu_node.counter:
                lfu_node = node
            node = node.next_node

        if (self.cache_len >= self.capacity):
            self.remove(lfu_node)

        self.appendleft(key, value)
        self.cache_len += 1

    def __str__(self):
        output = ''
        node = self.start_node
        while node != None:
            output += f"[{node.key}: {node.value} - {node.counter}],"
            node = node.next_node
        return f"[{output[:-1]}]"
