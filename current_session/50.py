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
        ans, neg = 1, True if n < 0 else False
        if neg:
            n, rec = -n, True
        while n != 1:
            if n % 2:
                n, ans = n-1, ans*x
            else:
                n, x = n/2, x*x
        return ans*x if not neg else 1/(ans*x)

print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))
