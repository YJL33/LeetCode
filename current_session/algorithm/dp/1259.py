from functools import lru_cache

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        # top-down dp
        @lru_cache(None)
        def dp(x):
            if x <= 4: return x//2
            # if x == 6: dp(6) = dp(4)+dp(2)*dp(2)+dp(2)*dp(2)+dp(4)
            # if x == 8: dp(8) = dp(6)+dp(2)*dp(4)+dp(4)*dp(2)+dp(6)
            # if x == 10: dp(10) = dp(8)+dp(2)*dp(6)+dp(4)*dp(4)+dp(6)*dp(2)+dp(8)
            # so on and so forth...
            return 2*dp(x-2) + sum([dp(a)*dp(x-2-a) for a in range(2, x-2, 2)])
        
        return dp(numPeople)%(1000000007)

    def numberOfWays(self, numPeople: int) -> int:
        # bottom-up dp
        dp = [i for i in range((numPeople//2)+1)]
        if numPeople <= 4: return dp[-1]
        # start from 6 = 2*x
        for x in range(3,(numPeople//2)+1):
            dp[x] = 2*dp[x-1] + sum(dp[a]*dp[x-1-a] for a in range(1,x-1))
        
        return dp[-1]%(1000000007)

print(Solution().numberOfWays(2))
print(Solution().numberOfWays(4))
print(Solution().numberOfWays(6))
print(Solution().numberOfWays(8))
print(Solution().numberOfWays(10))