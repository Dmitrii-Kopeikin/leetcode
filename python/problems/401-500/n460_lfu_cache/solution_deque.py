from collections import deque


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = deque(maxlen=capacity)

    def get(self, key: int) -> int:
        for item in self.cache:
            if item[0] == key:
                self.cache.remove(item)
                item[2] += 1
                self.cache.append(item)
                return item[1]

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        try:
            item_to_remove = self.cache[0]
        except IndexError:
            item_to_remove = None

        for item in self.cache:
            if item[0] == key:
                self.cache.remove(item)
                self.cache.append([key, value, item[2] + 1])
                return
            if item[2] < item_to_remove[2]:
                item_to_remove = item

        if len(self.cache) >= self.capacity:
            self.cache.remove(item_to_remove)
        self.cache.append([key, value, 1])

    def __str__(self):
        return f"{self.cache}"
