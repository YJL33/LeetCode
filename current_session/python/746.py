# constraints: 
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# use DP
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2: return min(cost)
        dp = [0 for _ in range(len(cost)+1)]
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[-1]

print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))