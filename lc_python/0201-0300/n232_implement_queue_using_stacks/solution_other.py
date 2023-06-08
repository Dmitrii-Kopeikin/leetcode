from typing import List


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            self._move_items()

        return self.s2.pop() if self.s2 else None

    def peek(self) -> int:
        if not self.s2:
            self._move_items()

        return self.s2[-1] if self.s2 else None

    def empty(self) -> bool:
        return not self.s2 and not self.s1
    
    def _move_items(self):
        while self.s1:
            self.s2.append(self.s1.pop())
