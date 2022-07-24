# use DP
# try all possible amounts
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [float('inf') for _ in range(amount+1)]
        coinSet = set(coins)
        for a in range(1,amount+1):
            if a in coinSet:
                dp[a] = 1
                continue
            for c in coins:
                if a-c > 0: dp[a] = min(dp[a], dp[a-c]+1)
            print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1

print(Solution().coinChange([1,2,5],11))
print(Solution().coinChange([2],3))
print(Solution().coinChange([1],0))
print(Solution().coinChange([1],1))
print(Solution().coinChange([1],2))