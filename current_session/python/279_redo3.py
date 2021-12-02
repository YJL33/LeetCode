import collections
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = collections.defaultdict(int)
        sqrt = int(math.sqrt(n))
        dp[0] = 0
        for t in range(1,n+1):
            # print('now sqrt = ', i)
            dp[t] = float('inf')
            for i in range(1,sqrt+1):
                if t-i*i >= 0 and t-i*i in dp:
                    if t in dp:
                        dp[t] = min(dp[t], 1+dp[t-i*i])
                    else:
                        dp[t] = 1+dp[t-i*i]
                    # print('t:', t, 'dp:', dp[t])
        
        return dp[n]

print(Solution().numSquares(12))
print(Solution().numSquares(13))
print(Solution().numSquares(100))
print(Solution().numSquares(2021))