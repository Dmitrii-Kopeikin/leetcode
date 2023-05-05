class Solution:
    def isHappy(self, n: int) -> bool:
        prevs = set()
        next = n
        while True:
            next = sum([int(d) ** 2 for d in str(next)])
            if next == 1:
                return True
            if next in prevs:
                return False
            prevs.add(next)