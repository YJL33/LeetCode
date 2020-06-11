"""
5431. Paint House III

There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n),
some houses that has been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.
(For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).

Given an array houses, an m * n matrix cost and an integer target where:

houses[i]: is the color of the house i, 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods,
if not possible return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5
Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
"""
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = {}

        def dfs(i, t, p):
            key = (i, t, p)         # compare with previous house
            # print "what's going on: ", key, dp

            if i == len(houses) or t < 0:
                # base case - we're trying to color 0 houses. Also catches the case where we accidentally
                # color in too many neighborhoods before or at the end of the array. t<0 isn't necesssary
                # to check here, but it prunes a little bit of the search space to make things slightly faster.
                return 0 if t == 0 else float('inf')
            
            if key not in dp:
                if houses[i] == 0:
                    tmp = []
                    for j in range(1, n+1):
                        # print "paint ", i, " as ", j
                        tmp += dfs(i + 1, t - (j != p), j) + cost[i][j - 1],
                    # print "tmp: ", tmp
                    dp[key] = min(tmp)
                    # dp[key] = min()
                else:
                    dp[key] = dfs(i + 1, t - (houses[i] != p), houses[i])
                
            return dp[key]
            
        ret = dfs(0, target, -1)
        # if ret is infinity, then we failed every case because there were too many neighborhoods
        # to start. If we could paint over houses that were previously painted, we could remedy that,
        # but the problem doesn't allow that. so, we return -1 in that case.
        return ret if ret < float('inf') else -1



# print Solution().minCost([0,0,0,0,0],[[1,10],[10,1],[10,1],[1,10],[5,1]],5,2,3)

print Solution().minCost([3,1,2,3],[[1,1,1],[1,1,1],[1,1,1],[1,1,1]],4,3,3)
# print Solution().minCost([4,0,0,0,4,11,0,0,0,0,3,0,0,0,0,5,0,0,0,0,0,8,2,2,0], [[33,13,38,3,25,10,49,9,10,36,39,3],[47,19,6,37,2,23,50,18,46,14,24,33],[32,31,32,17,36,41,43,29,36,29,47,3],[25,27,5,31,1,17,27,46,10,8,31,49],[50,16,33,24,42,2,33,39,43,31,2,38],[38,6,23,18,9,13,31,36,28,7,7,1],[40,23,21,5,48,2,18,24,6,27,39,44],[25,43,4,9,5,5,30,42,23,41,7,15],[45,32,44,15,5,1,2,43,49,30,29,4],[39,26,42,45,27,28,41,6,42,27,4,43],[32,2,43,13,15,30,32,12,36,5,19,22],[12,23,13,8,8,9,32,43,46,41,43,8],[10,18,27,2,7,40,44,50,32,29,42,10],[50,7,15,9,32,9,15,10,15,41,10,36],[48,6,26,6,14,37,44,47,4,44,1,30],[34,46,12,32,19,1,18,31,1,16,44,48],[15,35,17,14,16,29,23,18,28,26,45,17],[43,45,7,39,37,18,18,33,24,47,27,46],[17,12,15,20,44,34,14,8,28,40,12,21],[18,10,15,47,21,7,47,34,37,49,16,24],[19,3,38,14,32,21,4,25,34,3,33,23],[21,45,3,49,45,40,38,10,30,5,37,21],[29,38,43,22,44,26,3,18,45,40,40,17],[21,12,30,23,4,25,32,43,37,15,35,30],[38,14,6,21,3,43,43,30,9,19,39,17]],25,12,15)
# print Solution().minCost([0,0,0,0,0],[[1,10],[10,1],[10,1],[1,10],[5,1]],5,2,3)
print Solution().minCost([0,1,2,2,1],[[1,10],[10,1],[10,1],[1,10],[5,1]],5,2,3)
# print Solution().minCost([2,2,1],[[1,1],[3,4],[4,2]],3,2,2)