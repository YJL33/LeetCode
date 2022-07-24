from functools import lru_cache
from math import sqrt
# import sys
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # can remove any non-zero square number
        # sys.setrecursionlimit(550000)
        @lru_cache(None)
        def dp(n):
            if sqrt(n)%1 == 0: return True
            for i in range(1,int(sqrt(n))+1):
                # there's a way to make bob lose (definitely)
                if dp(n-i*i) is False: return True
            # no matter choose which one, bob will win
            return False
        return dp(n)

print(Solution().winnerSquareGame(100))
print(Solution().winnerSquareGame(200))
print(Solution().winnerSquareGame(300))
print(Solution().winnerSquareGame(1000))
