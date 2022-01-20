from functools import lru_cache
from typing import List
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        @lru_cache(None)
        def dfs(i, j, k):
            if k == j-i+1: return 0
            if k > j-i+1: return float('inf')
            if k == 1:
                m = houses[(i+j)//2]
                return sum(abs(x-m) for x in houses[i:j+1])
            
            return min(dfs(i,x,1) + dfs(x+1,j,k-1) for x in range(i, j) or [float('inf')])
        
        return dfs(0, len(houses)-1, k)