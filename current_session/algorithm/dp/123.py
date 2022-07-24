from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        # states: profit of empty-hand, hold 1st share, sold 1st share (empty-hand), hold 2nd share, done

        p1, h1, p2, h2, p3 = 0, float('-inf'), float('-inf'), float('-inf'), float('-inf')
        for i in range(len(prices)):
            b = max(h1, p1-prices[i])
            c = max(p2, h1+prices[i])
            d = max(h2, p2-prices[i])
            e = max(p3, h2+prices[i])
            h1, p2, h2, p3 = b,c,d,e

        return max(p1, h1, p2, h2, p3)