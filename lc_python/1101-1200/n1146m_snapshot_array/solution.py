from bisect import bisect_right


class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snap_id = 0
        self.snap_storage = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snap_storage[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect_right(self.snap_storage[index], [snap_id, 10 ** 9])
        return self.snap_storage[index][snap_index - 1][1]
