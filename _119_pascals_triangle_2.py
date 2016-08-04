"""
119. Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for r in xrange(1,rowIndex+1):
            res.append(0)                   # Extend the row by 1 unit
            for j in xrange(r,0,-1):        # Backward update the row
                res[j] += res[j-1]

        return res