"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # directly implement
        if not n: return False
        if n == 1: return True

        tmp = n
        sumup = 0

        while tmp:
            sumup += (tmp%10)**2
            tmp = tmp//10

        if sumup > 10:
            return self.isHappy(sumup)

        else:
            return sumup in [1,7,10]
