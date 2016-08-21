"""
386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space.
The input size may be as large as 5,000,000.
"""
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n <= 9:
            res = [i for i in xrange(1,n+1)]
        else:
            for i in xrange(1,10):
                res.append(i)
                self.helper(res, i, n)
        return res

    def helper(self, lst, i, n):
        timesTen = i*10
        if timesTen <= n:
            ceil = min(n-timesTen+1, 10)
            for j in xrange(ceil):
                ans = timesTen+j
                lst.append(ans)
                self.helper(lst, ans, n)

    def lexicalOrder2(self, n):
        res = [n for n in xrange(1,n+1)]
        res.sort(key=str)
        return res == self.lexicalOrder(n)