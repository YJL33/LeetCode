"""
 188. Best Time to Buy and Sell Stock IV

    Total Accepted: 35261
    Total Submissions: 150017
    Difficulty: Hard
    Contributors: Admin

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][j]: max profit until day j, using i transactions
        # dp[i][j] = max(dp[i][j-1], (price[j]- price[jj] + dp[i-1][jj]), jj in range(0, j-1)))
        # dp[0][j]: 0
        # dp[i][0]: 0
        n = len(prices)
        if n <= 1: return 0
        # if k >= n/2, then you can make maximum number of transactions.
        if k >= n/2:
            maxPro = 0
            for i in xrange(1,n):
                if prices[i] > prices[i-1]:
                    maxPro += prices[i] - prices[i-1]
            return maxPro

        dp = [[0 for _ in xrange(n)] for _ in xrange(k+1)]
        for i in xrange(1, k+1):
            localMax = dp[i-1][0] - prices[0]
            for j in xrange(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j]+localMax)
                localMax = max(localMax, dp[i-1][j]-prices[j])

        return dp[k][n-1]
