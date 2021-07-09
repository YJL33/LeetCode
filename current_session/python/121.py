"""
see https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        minPrice, maxProfit = prices[0], 0
        for p in prices[1:]:
            if p < minPrice:
                minPrice = p
            else:
                maxProfit = max(p-minPrice, maxProfit)
        return maxProfit
