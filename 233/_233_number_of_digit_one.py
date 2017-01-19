"""
 233. Number of Digit One

    Total Accepted: 24019
    Total Submissions: 89873
    Difficulty: Hard
    Contributors: Admin

Given an integer n,
count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

    Beware of overflow.
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0

        origin, digit, order, ans = n, 0, 1, 0
        while n:
            digit, n = n%10, n//10
            if digit == 1:
                ans += order*n+(origin%order+1)
            elif digit == 0:
                ans += order*n
            else:
                ans += order*(n+1)
            order *= 10
            #print "n: ", n, ", ans: ", ans
        return ans