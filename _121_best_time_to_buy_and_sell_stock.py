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
        if prices == []: return 0
        min_price = prices[0]           # the minimum price so far
        max_profit = 0                  # the maximum profit so far
        for p in prices:
            if p < min_price:
                min_price = p                       # update the minimum price
            else:
                if p - min_price > max_profit:
                    max_profit = p - min_price      # update the maximum profit
        return max_profit