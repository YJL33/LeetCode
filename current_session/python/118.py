"""
118
"""
from typing import List
class Solution:
    def generate(self, N: int) -> List[List[int]]:
        if N == 1: return [[1]]
        if N == 2: return [[1],[1,1]]
        res = [[1], [1,1]]
        while len(res) < N:
            x = res[-1]
            res.append([1]+[x[i]+x[i+1] for i in range(len(x)-1)]+[1])
        return res
