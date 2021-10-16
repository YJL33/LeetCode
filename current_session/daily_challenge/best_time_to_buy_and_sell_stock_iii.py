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

print(Solution().maxProfit(prices = [3,3,5,0,0,3,1,4]))
print(Solution().maxProfit(prices = [1,2,3,4,5]))
print(Solution().maxProfit(prices = [7,6,5,2,1]))
print(Solution().maxProfit(prices = [1]))
print(Solution().maxProfit(prices = [2,4,1]))
print(Solution().maxProfit(prices = [6,1,3,2,4,7]), 'should be 7')
