from functools import lru_cache

class Solution:
    
    def maxA(self, n: int) -> int:
        # basically we have 2 moves:
        # 1 move: count+1
        # 3 moves: copy-paste
        # at least need 3 moves to do copy-paste, then we can paste as many as we want
        # use top-down DP
        # dp[n] is the solution of n
        
        @lru_cache
        def dp(x):
            if x <= 6: return x
            res = x
            for i in range(x-2):        # max i = x-3
                res = max(res, dp(i)*(x-i-1))
            return res

        return dp(n)

