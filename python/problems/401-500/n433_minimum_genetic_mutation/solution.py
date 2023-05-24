from typing import List, Optional
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def is_valid_mutation(gene: str, other_gene: str):
            count = 0
            for i in range(8):
                if gene[i] != other_gene[i]:
                    count += 1
            return count == 1

        visited = set([startGene])
        quaue = deque([(startGene, 0)])

        while quaue:
            start_gene, steps = quaue.pop()
            if start_gene == endGene:
                return steps
            for gene in bank:
                if gene not in visited and is_valid_mutation(start_gene, gene):
                    visited.add(gene)
                    quaue.appendleft((gene, steps + 1))

        return -1
