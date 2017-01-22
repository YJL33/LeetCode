"""
279. Perfect Squares

Given a positive integer n,
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example,
given n = 12, return 3 because 12 = 4 + 4 + 4;
given n = 13, return 2 because 13 = 4 + 9.
"""
# Refer to http://www.cnblogs.com/grandyang/p/4800552.html
# Not a DP solution
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        import math
        import itertools
        print n
        upper_bound = int(math.floor(math.sqrt(n)))
        candidates = [pow(x,2) for x in xrange(upper_bound+1)]
        for pair in itertools.product(candidates, repeat=2):
            if sum(pair) == n:
                return (pair[0]>0)+(pair[1]>0)
        return 3
