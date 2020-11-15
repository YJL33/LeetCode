"""
https://leetcode.com/problems/coin-change-2/
"""
class Solution(object):
    def __init__(self):
        self.tmp = {}

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        return self.helper(amount, coins)

    def helper(self, amount, coins):
        if amount == 0:
            return 1
        if not coins:
            return 0
        if len(coins) == 1:
            return 1 if (amount%coins[0]==0) else 0
        if coins[-1] > amount:
            return self.helper(amount, coins[:-1])

        numOfBiggest = amount//coins[-1]
        res = 0
        while numOfBiggest >= 0:
            tmp = amount-coins[-1]*numOfBiggest
            if (tmp, len(coins)-1) not in self.tmp:
                sol = self.helper(tmp, coins[:-1])
                self.tmp[(tmp, len(coins)-1)] = sol
            else:
                sol = self.tmp[(tmp, len(coins)-1)]
            res += sol
            numOfBiggest -= 1
        return res

print(Solution().change(amount = 5, coins = [1, 2, 5]))
print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 10, coins = [10] ))
print(Solution().change(500,[1,2,5]), 'should be 12701')
print(Solution().change(500,[3,5,7,8,9,10,11]))