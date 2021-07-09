"""
256
"""
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0: return 0
        if len(costs) == 1: return min(costs[0])

        # DP
        dp = costs[0]
        for i in range(1, len(costs)):
            prev = [x for x in dp]
            for j in range(3):
                dp[j] = min(prev[(j+1)%3],prev[(j+2)%3])+costs[i][j]
        
        return min(dp)

# print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))
# print(Solution().minCost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]))
# print(Solution().minCost([]))
# print(Solution().minCost([[7,2,6]]))
