"""
https://leetcode.com/problems/powx-n/
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        ans, neg = 1, n<0
        while n:
            if n%2:
                ans, n = ans*x, n-1
            else:
                x, n = x*x, n/2


print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))
