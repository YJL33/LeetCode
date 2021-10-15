from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use DP
        # dp[i] = already bought, buy, sell, no CD at that day
        # already bought = max(already bought, bought at i-1)
        # buy at i = max( bought at i-1, no CD at i-1 - prices[i])
        # sell at i = prices[i]+(bought at i-1)
        # no CD (sold) at i = max(sold at i-1, no CD at i-1)

        dp = [float('-inf'), -prices[0], 0, 0]
        for i in range(1,len(prices)):
            prevAB, prevBought, prevSold, prevNoCD = dp
            a = max(prevAB, prevBought)
            b = max(prevBought, prevNoCD-prices[i])
            s = prices[i]+max(prevBought, prevAB)
            n = max(prevSold, prevNoCD)
            dp = [a,b,s,n]
            # print("DP at i", i, dp)
        
        return max(dp)

print(Solution().maxProfit([1,2,3,0,2]))
print(Solution().maxProfit([1]))
