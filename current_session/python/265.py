from typing import List
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        dp = costs[0]

        for i in range(1,len(costs)):
            tmp = costs[i]
            for j in range(len(tmp)):
                add = float('inf')
                for k in range(len(dp)):
                    if k == j: continue
                    add = min(add, dp[k])
                tmp[j] += add
            dp = tmp
        
        return min(dp)

print(Solution().minCostII([[20,19,11,13,12,16,16,17,15,9,5,18],[3,8,15,17,19,8,18,3,11,6,7,12],[15,4,11,1,18,2,10,9,3,6,4,15]]))