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
        h, w = bm.dimensions()
        # find the 1st row
        r = 0
        while r < h and bm.get(r, w-1) == 0:
            r += 1
        if r == h:
            return -1

        ans = w-1
        # find the 1st 1 in all rows
        # find the better solution in this row if possible
        for i in range(r, h):
            if bm.get(i, ans) == 1:
                ans = self.helper(i, ans, bm)
        return ans


    def helper(self, row, r, bm):
        l = 0
        while l < r:
            m = l + (r-l)//2
            if bm.get(row, m) == 1:     # check the left side
                r = m
            else:                       # check the right side
                l = m+1
        return l
