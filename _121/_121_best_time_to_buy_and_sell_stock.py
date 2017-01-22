"""
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0       # corner case: []
        minprice, maxgain = prices[0], 0
        for p in prices[1:]:
            if p < minprice:
                minprice = p
            else:
                maxgain = max(maxgain, p-minprice)
        return maxgain