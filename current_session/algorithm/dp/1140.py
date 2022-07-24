from functools import lru_cache
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # both play optimally
        # use suffix sum
        # use DP
        N = len(piles)
        suffix_sum = [x for x in piles]
        for i in range(N-2, -1, -1):
            suffix_sum[i] += suffix_sum[i+1]

        @lru_cache(None)
        def dp(i, m):
            if i+2*m >= N: return suffix_sum[i]
            return suffix_sum[i]-min(dp(i+x, max(m,x)) for x in range(1, 2*m+1))
        
        return dp(0, 1)