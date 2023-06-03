from typing import List
from math import gcd, sqrt
from collections import defaultdict, deque


class Solution:
    def canTraverseAllPairs(self, nums):
        n = len(nums)
        if n == 1:
            return True
        union_dict = defaultdict(int)

        def find(node):
            if node not in union_dict:
                return node
            else:
                if node != union_dict[node]:
                    union_dict[node] = find(union_dict[node])
                return union_dict[node]

        def union(node, other_node):
            a, b = find(node), find(other_node)
            if a != b:
                union_dict[b] = a

        res = [-1]*(max(nums) + 1)

        for i, value in enumerate(nums):
            if value == 1:
                return False
            for divisor in range(2, int(sqrt(value)) + 1):
                if value % divisor != 0:
                    continue
                if res[divisor] != -1:
                    union(res[divisor], i)
                else:
                    res[divisor] = i
                while value % divisor == 0:
                    value //= divisor

            if value > 1:
                if res[value] != -1:
                    union(res[value], i)
                else:
                    res[value] = i

        group_id = find(0)
        for i in range(1, n):
            if find(i) != group_id:
                return False
            
        return True
