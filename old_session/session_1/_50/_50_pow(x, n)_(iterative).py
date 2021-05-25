"""
50. Pow(x, n)

Implement pow(x, n).
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Iterative version
        if n == 0: return 1
        ans, rec = 1, False   # reciprocal
        while n != 1:
            if n < 0:
                n, rec = -n, True
            elif n % 2:
                n, ans = n-1, ans*x
            else:
                n, x = n/2, x*x
        return ans*x if not rec else 1/(ans*x)
            
        