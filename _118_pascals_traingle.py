"""
118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        res = [[1]]
        for r in xrange(1,numRows):
            res.append([0]*(r+1))                   # generate current row
            for j in xrange(r):
                res[r][j+1] += res[r-1][j]          # add each element in earlier row
                res[r][j] += res[r-1][j]            # into both element in current row

        return res