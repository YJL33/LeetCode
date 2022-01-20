from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # similar as iii
        # dp_hold: hold ith stock
        # dp_sold: sold ith stock
        dp_hold = [float('-inf') for _ in range(k)]
        dp_sold = [0]+[float('-inf') for _ in range(k)]

        for i in range(len(prices)):
            p = prices[i]
            tmp_hold, tmp_sold = [], [0]
            for j in range(k):
                tmp_hold.append(max(dp_hold[j], dp_sold[j]-p))
                tmp_sold.append(max(dp_sold[j+1], dp_hold[j]+p))
            dp_hold, dp_sold = tmp_hold, tmp_sold

        return max(dp_sold, dp_hold)

print(Solution().maxProfit(10, [3,2,6,5,0,3,1,5,6,7,9,2,4,1,27,6,5,1,25,34,3,13,3]), 'should be 86')