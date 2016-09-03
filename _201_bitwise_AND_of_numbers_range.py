"""
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # amortize: O(log(m) + log(n))
        def l2(x): return len(bin(x))-3

        res = 0
        while l2(m) == l2(n) and m > 0 and n > 0:
            res, m, n = res+(1<<l2(m)), m-(1<<l2(m)), n-(1<<l2(n))
            #print res
        return res