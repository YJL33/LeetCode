"""
https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, bm):
        """
        :type bm: BinaryMatrix
        :rtype: int
        """
        # for each row, find first col with 1
        ans = -1
        h, w = bm.dimensions()
        col = w-1
        for i in range(h):
            if bm.get(i, col) == 1:
                ans = self.helper(i, col, bm)
                col = ans
        return ans

    def helper(self, row, r, bm):
        # given row, use binary search to find first column has 1
        l = 0
        # find the bisect_left of 1
        while l<r:
            m = l + (r-l)//2
            if bm.get(row, m) == 1:
                r = m
            else:
                l = m+1
        return l