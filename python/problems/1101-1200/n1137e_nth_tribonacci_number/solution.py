class Solution:
    def tribonacci(self, n: int) -> int:
        numbers = [0, 1, 1] + [0] * (n - 2)
        for i in range(3, n + 1):
            numbers[i] = sum(numbers[i - 3: i])

        return numbers[n]
    
    # cache = None

    # def tribonacci(self, n: int) -> int:
    #     if self.cache is None:
    #         self.cache = [0, 1, 1] + [-1] * (n - 2)

    #     print(self.cache, n)
    #     if self.cache[n] != -1:
    #         return self.cache[n]

    #     for i in [n - 1, n - 2, n - 3]:
    #         if self.cache[i] == -1:
    #             self.cache[i] = self.tribonacci(i)

    #     self.cache[n] = self.cache[n - 1] + self.cache[n - 2] + self.cache[n - 3]

    #     return self.cache[n]

