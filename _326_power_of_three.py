"""
326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # use while loop
        if n <= 0:
            return False
        while not n%3:
            n /= 3
        return n == 1

    def isPowerOfThree2(self, value):
        return value > 0 and 1162261467%value == 0