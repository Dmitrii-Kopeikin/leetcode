from functools import reduce


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # binary_x = bin(x)[2::]
        # binary_y = bin(y)[2::]
        # binary_x = binary_x.zfill(len(binary_y))
        # binary_y = binary_y.zfill(len(binary_x))

        # print([x != y for x, y in list(zip(binary_y, binary_x))])
        # print(max(binary_y, binary_x))

        # print(binary_x)
        # print(binary_y)
        print(sum([x == '1' for x in bin(x ^ y)]))
        print(len(bin(x ^ y).replace('0', '')) - 1)
        print(len(f"{x ^ y:b}".replace('0', '')))
        print(reduce(lambda s, v: int(s) + int(v), list(f"{x ^ y:b}")))

        # return sum([x != y for x, y in list(zip(binary_y, binary_x))])


solution = Solution()
print(solution.hammingDistance(1, 4))
print(solution.hammingDistance(93, 73))
print(solution.hammingDistance(4, 14))
