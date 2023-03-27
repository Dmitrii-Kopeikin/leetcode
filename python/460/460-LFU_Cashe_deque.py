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
