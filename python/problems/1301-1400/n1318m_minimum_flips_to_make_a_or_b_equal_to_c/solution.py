from typing import List


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count('1') + bin(a & b & ~ c).count('1')


    # def minFlips(self, a: int, b: int, c: int) -> int:

    #     def get_bit(value: int, index: int) -> int:
    #         return (value >> index) & 1

    #     def invert(bit: int) -> int:
    #         return int(not bit)

    #     flips_count = 0
    #     for i in range(len(bin(max(a, b, c))) - 2):
    #         a_bit = get_bit(a, i)
    #         b_bit = get_bit(b, i)
    #         c_bit = get_bit(c, i)

    #         if a_bit | b_bit == c_bit:
    #             continue
    #         if (invert(a_bit) | b_bit) == c_bit or (a_bit | invert(b_bit)) == c_bit:
    #             flips_count += 1
    #         else:
    #             flips_count += 2

    #     return flips_count
