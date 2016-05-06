"""
70. Climbing Stairs

You are climbing a stair case.
It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        if n >= 3:
            one_step = 2        # number of distinct ways for n = n-1
            two_steps = 1       # number of distinct ways for n = n-2
            res = 0
            for i in xrange(3,n+1):
                res = two_steps + one_step      # res = answer
                two_steps = one_step            # update
                one_step = res
        return res