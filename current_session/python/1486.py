class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arr = [start+2*i for i in xrange(n)]
        res = 0
        for a in arr:
            res = res ^ a
        
        return res

    