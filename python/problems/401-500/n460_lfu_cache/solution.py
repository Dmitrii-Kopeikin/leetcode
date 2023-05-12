from collections import deque


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_len = 0
        self.cache = {}

    def get(self, key: int) -> int:
        try:
            item = self.cache[key]
            del self.cache[key]
            item[1] += 1
            self.cache[key] = item
            return item[0]
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        key_to_del = None
        counter = 0
        for item in self.cache.items():
            if item[1][1] < counter or key_to_del == None:
                key_to_del = item[0]
                counter = item[1][1]

            if item[0] == key:
                item = self.cache[key]
                del self.cache[key]
                item = [value, item[1] + 1]
                self.cache[key] = item
                return

        if self.cache_len >= self.capacity:
            del self.cache[key_to_del]

        self.cache[key] = [value, 1]
        self.cache_len += 1

    def __str__(self):
        return f"{self.cache}"
