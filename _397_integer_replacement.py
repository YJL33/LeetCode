"""
397. Integer Replacement

Given a positive integer n and you can do operations as follow:

    If n is even, replace n with n/2.
    If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?
"""
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the minimum distance b/w 2^n
        return self.helper(n)

    def helper(self, n, counter=0):
    	if n == 1:
    		return counter
    	if not n%2:
    		return self.helper(n/2, counter+1)
    	else:
    		return min(self.helper(n+1, counter+1), self.helper(n-1, counter+1))
