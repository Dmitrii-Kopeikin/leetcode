class Solution:
    def fib(self, n: int) -> int:
        numbers = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            numbers[i] = sum(numbers[i - 2: i])

        return numbers[n]


    # cache = None

    # def fib(self, n: int) -> int:
    #     if self.cache is None:
    #         self.cache = [0, 1] + [-1] * (n - 1)

    #     if self.cache[n] != -1:
    #         return self.cache[n]

    #     for i in [n - 1, n - 2]:
    #         if self.cache[i] == -1:
    #             self.cache[i] = self.fib(i)

    #     self.cache[n] = self.cache[n - 1] + self.cache[n - 2]

    #     return self.cache[n]
