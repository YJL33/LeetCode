"""
69. Sqrt(x)

Implement int sqrt(int x).
Compute and return the square root of x.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        # Implement Newton method:
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
        """
        # Implement Binary Search:
        if x == 0:
            return 0
        left = 1        # lower bound
        right = x       # upper bound
        while True:
            mid = left + (right-left)/2         # prevent the overflow: right+left may exceed limit
            if mid > (x/mid):                   # mid > sqrt, so decrease upper bound
                right = mid - 1
            else:                               # mid <= sqrt, so increase lower bound
                if mid+1 > x/(mid+1):
                    return mid                  # return the answer
                left = mid + 1