# Last updated: 6/25/2025, 4:10:06 AM
from collections import deque
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if end not in bank:
            return -1

        queue = deque([(start, 0)])
        visited = {start}
        nucleotides = ['A', 'G', 'C', 'T']

        while queue:
            current_gene, mutations = queue.popleft()
            if current_gene == end:
                return mutations

            for i in range(len(current_gene)):
                for nucleotide in nucleotides:
                    next_gene_list = list(current_gene)
                    if next_gene_list[i] != nucleotide:
                        next_gene_list[i] = nucleotide
                        next_gene = "".join(next_gene_list)
                        if next_gene in bank and next_gene not in visited:
                            visited.add(next_gene)
                            queue.append((next_gene, mutations + 1))

        return -1