from functools import lru_cache
from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        N = len(stoneValue)
        
        @lru_cache(None)
        def finder(i):
            if i >= N: return 0
            diff = []
            take = 0
            for j in range(i, min(i+3, N)):
                take += stoneValue[j]
                diff.append(take-finder(j+1))
            return max(diff)
        
        x = finder(0)
        if x == 0:
            return "Tie"
        elif x > 0:
            return "Alice"
        else:
            return "Bob"


    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # bottom up
        N = len(stoneValue)
        dp = [float('-inf') for _ in range(N)]

        for i in range(N-1, -1, -1):
            take = 0
            for j in range(i, min(i+3, N)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take-dp[j+1] if j+1 < N else take)
        
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"
