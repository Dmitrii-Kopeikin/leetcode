from collections import deque

class RecentCounter:
    
    def __init__(self):
        self.requests = deque()
        self.requests_len = 0

    def ping(self, t: int) -> int:
        self.append(t)
        return self._ping()

    def append(self, t: int):
        self.requests.append(t)
        self.requests_len += 1

    def _ping(self) -> int:
        border = self.requests[-1] - 3000
        while self.requests[0] < border:
            self.requests.popleft()
            self.requests_len -= 1
        return self.requests_len