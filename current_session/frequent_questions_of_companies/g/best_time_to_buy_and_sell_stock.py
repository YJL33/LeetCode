from typing import List
class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        buy, noBuy = prices[0], 0           # buy price at day i
        dp = [0]
        for p in prices[1:]:
            dp.append(max(noBuy, p-buy))
            buy = min(p, buy)

        return max(dp)

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))