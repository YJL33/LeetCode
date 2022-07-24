from typing import List
from functools import cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # must try all posibilities
        # top down dp
        # dp(i, k) is the solution of using piles[:i+1] , and take k piles of coins
        # for each new pile j, you can take from 0 piles to min(k, pile[j]) piles coins from piles[j]
        
        N = len(piles)
        
        @cache
        def dp(i, k):
            # termination
            if i == 0:
                return sum(piles[i][:k])
           
            # take
            res = dp(i-1, k)            # take nothing
            prefix_sum, take = 0, 0
            for j in range(min(k, len(piles[i]))):
                prefix_sum += piles[i][j]
                take += 1
                if k >= take:           # only take possible piles
                    res = max(res, prefix_sum+dp(i-1, k-take))
            return res
        
        return dp(N-1, k)