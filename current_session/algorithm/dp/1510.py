from functools import cache
from math import sqrt
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # can remove any non-zero square number
        @cache
        def dp(n):
            if sqrt(n)%1 == 0: return True
            for i in range(1,int(sqrt(n))+1):
                # there's a way to win
                if dp(n-i*i) is False: return True
            # no matter choose which one, bob will win
            return False
        return dp(n)
        
    def winnerSquareGame(self, n: int) -> bool:
        # bottom-up
        dp = [-1 for _ in range(n+1)]
        dp[0] = False
        dp[1] = True
        for i in range(2, n+1):
            dp[i] = False
            if sqrt(n)%1 == 0:
                dp[i] = True
            else:
                for j in range(1, int(sqrt(n))+1):
                    if dp[i-j*j] is False:
                        dp[i] = True
        
        # print('dp', dp)
        return dp[n]