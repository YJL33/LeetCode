"""
https://leetcode.com/problems/coin-change-2/
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for c in coins:
            for j in range(1, amount+1):
               if j >= c:
                   dp[j] += dp[j-c]
        return dp[amount]


print(Solution().change(amount = 5, coins = [1, 2, 5]))
print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 10, coins = [10] ))
print(Solution().change(500,[1,2,5]), 'should be 12701')
print(Solution().change(500,[3,5,7,8,9,10,11]), 'should be 35502874')