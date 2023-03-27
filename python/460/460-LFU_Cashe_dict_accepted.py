from queue import Queue


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_len = 0
        self.cache = dict()
        self.cache[0] = dict()

    def get(self, key: int) -> int:
        for main_key, bucket in self.cache.items():
            if key in bucket.keys():
                value = bucket[key]
                if (not main_key + 1 in self.cache.keys()) or self.cache[main_key + 1] is None:
                    self.cache[main_key + 1] = dict()
                self.cache[main_key + 1][key] = bucket[key]
                del bucket[key]
                return value

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        for main_key, bucket in self.cache.items():
            if key in bucket.keys():
                bucket[key] = value
                if (not (main_key + 1) in self.cache.keys()) or self.cache[main_key + 1] is None:
                    self.cache[main_key + 1] = dict()
                self.cache[main_key + 1][key] = bucket[key]
                del bucket[key]
                return

        if self.current_len >= self.capacity:
            is_lfu_removed = False
            for main_key, bucket in self.cache.items():
                for bucket_key in bucket.keys():
                    del bucket[bucket_key]
                    self.current_len += 1
                    is_lfu_removed = True
                    break
                if is_lfu_removed:
                    break

        self.cache[0][key] = value
        self.current_len += 1

    def __str__(self):
        return f"{self.cache.items()}"


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lfu_cache = LFUCache(0)
lfu_cache.put(0, 0)
print(lfu_cache)
print(lfu_cache.get(0))
print(lfu_cache)

print("---")

lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
print(lfu_cache)
lfu_cache.put(2, 2)
print(lfu_cache)
lfu_cache.get(1)
print(lfu_cache)
lfu_cache.put(3, 3)
print(lfu_cache)
lfu_cache.get(2)
print(lfu_cache)
lfu_cache.get(3)
print(lfu_cache)
lfu_cache.put(4, 4)
print(lfu_cache)
lfu_cache.get(1)
print(lfu_cache)
lfu_cache.get(3)
print(lfu_cache)
lfu_cache.get(4)

print("---")

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
print(lfu_cache.get(2))
print(lfu_cache.get(2))
print(lfu_cache.get(3))
print(lfu_cache.get(4))

print("---")

lfu_cache = LFUCache(4)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
lfu_cache.put(3, 3)
lfu_cache.put(4, 4)
lfu_cache.get(1)
lfu_cache.get(2)
lfu_cache.put(5, 5)
lfu_cache.put(6, 6)
print(lfu_cache)
lfu_cache.put(7, 7)
print(lfu_cache)
