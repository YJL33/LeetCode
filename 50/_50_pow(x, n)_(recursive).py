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
        # Recursive: Consider n=0, n<0, n>0
        if n is 0:
            return 1
        if n < 0:         # Consider negative case earlier than positive
            # 2^-1 = 1/2, 2^-2= 1/4 2^-3 = 1/8 ....
            return 1 / self.myPow(x, -n)
        if n % 2:         # n is not 2*k
            return x*self.myPow(x, n-1)
        else:             # n is 2*k
            return self.myPow(x*x, n/2)
