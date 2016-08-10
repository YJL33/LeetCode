"""
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free1, free2, hold1, hold2 = 0, 0, float('-inf'), float('-inf')
        for p in prices:
            free1, hold1 = max(free1, (hold1+p)), max(hold1, -p)
            free2, hold2 = max(free2, (hold2+p)), max(hold2, free1-p)
            #print free1, hold1, free2, hold2
        return free2
