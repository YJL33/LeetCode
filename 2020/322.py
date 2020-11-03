"""
see https://leetcode.com/problems/coin-change/
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # use dp: dp[i] is answer of amount = i
        # time complexity: O(amt*len(coins)), 

        MAX = float('inf')
        dp = [MAX for _ in range(amount+1)]
        dp[0] = 0

        for amt in range(1, amount+1):
            tmp = [MAX]
            for c in coins:
                if amt >= c:
                    tmp += dp[amt-c]+1,      # use this coin
            dp[amt] = min(tmp)

        return dp[-1] if dp[-1] != MAX else -1

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1], 1))
print(Solution().coinChange([1], 2))
