"""
1615
"""
from typing import List
import collections
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rds = set()
        nd = collections.defaultdict(int)
        for r in roads:
            a, b = r[0], r[1]
            rds.add((min(a,b), max(a,b)))
            nd[a] += 1
            nd[b] += 1
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                tmp = nd[i]+nd[j]
                if (i,j) in rds:
                    tmp -= 1
                ans = max(ans, tmp)
        
        return ans