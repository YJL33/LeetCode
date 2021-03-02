"""
1029
"""
from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # consider savings
        # high saving = go to A is cheaper(better)
        savings = []
        L = len(costs)
        for i in range(L):
            savings.append((costs[i][1]-costs[i][0], i))
        
        savings.sort()      # lower saving is priorized
        # print(savings)
        As, Bs = 0, 0
        for s in savings[:L//2]:
            As += costs[s[1]][1]
        for s in savings[L//2:]:
            Bs += costs[s[1]][0]
        
        return As+Bs