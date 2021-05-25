"""
231. Power of Two

Given an integer,
write a function to determine if it is a power of two.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while not n%2:
            n = n >> 1

        return n == 1