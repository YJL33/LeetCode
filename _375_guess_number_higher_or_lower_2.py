"""
375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

Given a particular n ≧ 1, find out how much money you need to have to guarantee a win.

The best strategy to play the game is to minimize the maximum loss you could possibly face.
Another strategy is to minimize the expected loss.
Here, we are interested in the first scenario.
Take a small example (n = 3). What do you end up paying in the worst case?

The purely recursive implementation of minimax would be worthless for even a small n.
You MUST use dynamic programming.

As a follow-up, how would you modify the code to solve the problem of minimizing the expected loss,
instead of the worst-case loss?
"""
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def cost(arr, start, end):
            res = float('inf')
            if start >= end:
                return 0
            if arr[start][end] != 0:
                return arr[start][end]

            for i in xrange(start, end+1):
                temp = i + max(cost(arr, start, i-1), cost(arr, i+1, end))   # Key point here
                if temp < res:
                    res = temp

            arr[start][end] = res
            return res

        dp = [[0 for i in xrange(n+1)] for j in xrange(n+1)]
        return cost(dp, 1, n)
