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
        # use dp: dp[i+x] = dp[i]+1 if x in coins
        if amount == 0: return 0
        if amount in coins: return 1

        dp = [float('inf') for _ in range(amount+1)]

        for c in coins:
            if c <= amount:
                dp[c] = 1
        for a in range(amount+1):
            if dp[a] != 1:
                comb = []
                for c in coins:
                    comb += dp[max(0,a-c)]+1,
                dp[a] = min(comb)

        return dp[-1] if dp[-1] != float('inf') else -1

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1], 1))
print(Solution().coinChange([1], 2))
