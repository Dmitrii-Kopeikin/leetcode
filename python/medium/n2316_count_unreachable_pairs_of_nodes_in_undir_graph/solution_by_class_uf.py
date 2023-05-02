from collections import Counter


class UnionFind:
    def __init__(self, size):
        # list of sets(groups)
        # in the beginning we have size number of sets
        self.root = [i for i in range(size)]

        self.rank = [1] * size

    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node_a, node_b):
        # find indexes of sets which nodes belong
        root_a = self.find(node_a)
        root_b = self.find(node_b)
        # if nodes belong to one set, nothing to do
        if root_a != root_b:
            # we compare sets ranks which nodes belong,
            # and place both nodes in set with bigger rank
            if self.rank[root_a] > self.rank[root_b]:
                self.root[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.root[root_a] = root_b
            else:
                # if ranks of sets is equal, we unite them and increment rank
                # of result set
                self.root[root_b] = root_a
                self.rank[root_a] += 1


class Solution:

    def count_pairs(self, n: int, edges: list[list[int]]) -> int:
        union_finder = UnionFind(n)
        for node_a, node_b in edges:
            union_finder.union(node_a, node_b)
        groups_with_sizes = Counter([union_finder.find(i) for i in range(n)])
        group_sizes = list(groups_with_sizes.values())
        result = 0
        first_group_size = group_sizes[0]
        for i in range(1, len(group_sizes)):
            result += first_group_size * group_sizes[i]
            first_group_size += group_sizes[i]
        return result


if __name__ == '__main__':
    solution = Solution()
    dataset = [
        # (3, [[0, 1], [0, 2], [1, 2]], 0),
        # (3, [[1, 2], [0, 2], [0, 1]], 0),
        (7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14),
    ]
    for data in dataset:
        print(solution.count_pairs(data[0], data[1]))
