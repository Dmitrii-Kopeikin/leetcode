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

        # if key in self.cache:
        #     item = self.cache[key]
        #     del self.cache[key]
        #     item = [value, item[1] + 1]
        #     self.cache[key] = item
        #     return

        # if self.cache_len >= self.capacity:
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

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# lfu_cache = LFUCache(0)

# lfu_cache.put(0, 0)
# print(lfu_cache)
# print(lfu_cache.get(0))
# print(lfu_cache)


# lfu_cache = LFUCache(2)
# lfu_cache.put(1, 1)
# print(lfu_cache)
# lfu_cache.put(2, 2)
# print(lfu_cache)
# lfu_cache.get(1)
# print(lfu_cache)
# lfu_cache.put(3, 3)
# print(lfu_cache)
# lfu_cache.get(2)
# print(lfu_cache)
# lfu_cache.get(3)
# print(lfu_cache)
# lfu_cache.put(4, 4)
# print(lfu_cache)
# lfu_cache.get(1)
# print(lfu_cache)
# lfu_cache.get(3)
# print(lfu_cache)
# lfu_cache.get(4)


lfu_cache = LFUCache(2)
print(lfu_cache)
lfu_cache.put(2, 1)
print(lfu_cache)
lfu_cache.put(2, 2)
print(lfu_cache)
print(lfu_cache.get(2))
lfu_cache.put(1, 1)
print(lfu_cache)
lfu_cache.put(4, 1)
print(lfu_cache)
print(lfu_cache.get(2))
print(lfu_cache)
# print(lfu_cache.get(2))
# print(lfu_cache.get(2))
# print(lfu_cache.get(3))
# print(lfu_cache.get(4))


# lfu_cache = LFUCache(4)
# lfu_cache.put(1, 1)
# lfu_cache.put(2, 2)
# lfu_cache.put(3, 3)
# lfu_cache.put(4, 4)
# lfu_cache.get(1)
# lfu_cache.get(2)
# lfu_cache.put(5, 5)
# lfu_cache.put(6, 6)
# print(lfu_cache)
# lfu_cache.put(7, 7)
# print(lfu_cache)
