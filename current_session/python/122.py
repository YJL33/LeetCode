from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, notBuy = -1*prices[0], 0
        for i in range(1, len(prices)):
            buy, notBuy = max(buy, notBuy-prices[i]), max(notBuy, buy+prices[i])
        
        return notBuy