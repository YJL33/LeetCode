"""
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time 
    (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day.
    (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        There are three states:
        free: max profit that free to buy stock at day N.
        hold: max profit that hold stock at day N.
        cooldown: max profit that (being forced to) do nothing (rest) at day N.

        At day i:
        free => maxprofits should be either
            1. free at day i-1, rest at day i
            2. cooldown at day i-1, rest at day i
        hold => maxprofits should be either
            1. free at day i-1, and BUY at day i (minus profit at price P[i-1]).
            2. hold at day i-1 (having stock), and rest at day i
        cooldown => SELL at day i-1
            => must be holding at day i-1, and SELL at day i-1 (add profit at price P[i-1])

        Therefore, we need to know the status before day 0:
        free => should be 0
        hold => violate assumption      => shouldn't influence future value
        cooldown => violate assumption  => shouldn't influence future value
        """
        free, hold, cooldown = 0, float('-inf'), float('-inf')
        for p in prices:
            free, hold, cooldown = max(free, cooldown), max(hold, free - p), (hold + p)
        return max(free, cooldown)      # We only need to check free and cooldown.