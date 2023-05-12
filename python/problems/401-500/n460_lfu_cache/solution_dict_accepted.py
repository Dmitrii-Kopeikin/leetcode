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
