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

    def push(self, x: int) -> None:
        temp = []
        for _ in range(len(self.s1)):
            temp.append(self.s1.pop())
        self.s1.append(x)
        for _ in range(len(temp)):
            self.s1.append(temp.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0
