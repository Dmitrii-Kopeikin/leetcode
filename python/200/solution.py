from collections import Counter


class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        l1 = ['1', '2', '3', '4']
        l2 = ['1', '1']

        c1 = Counter('rkqodlw')
        c2 = Counter('world')

        for key, value in c2.items():
            if key in c1:
                if c2[key] > c1[key]:
                    print(False)
            else:
                print(False)

        return 0


if __name__ == '__main__':
    Solution().num_islands(list(list()))
