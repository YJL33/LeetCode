from typing import List
from functools import cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # use DP top-down
        # try each cut first

        # time analysis: sorting, dp
        # space analysis: cache, left&right manipulation

        # optimization: use bitwise

        N = len(cuts)
        cuts.sort()
        bitwise = (1<<N)-1
        
        @cache
        def dp(start, end, bit):
            if bit == 0: return 0

            cost = end-start
            res = float('inf')
            left, right = 0, bit
            
            # try each cut first
            for i in range(N):
                c = cuts[i]
                if (1<<i)&bit and start < c < end:
                    right = right^(1<<i)
                    res = min(res, cost+dp(start, c, left)+dp(c, end, right))
                    left = left|(1<<i)
            return res

        return dp(0, n, bitwise)

print(Solution().minCost(7, [1,3,4,5]))