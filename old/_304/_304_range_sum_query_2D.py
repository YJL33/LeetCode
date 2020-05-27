"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix,
find the sum of the elements inside the rectangle,
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≦ row2 and col1 ≦ col2.
"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        # Construct 1D-sum array as #303.
        self.dp = []
        for i in xrange(len(matrix)):
            self.dp.append([0])
            for n in matrix[i]:                         # For each n in each row (row i) ...
                self.dp[i].append(self.dp[i][-1] + n)   # NumMatrix.dp[i][n] = sum from 0 to n in row i
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Add 1D-sum first (from col1 to col2), then add these (from row1 to row2) up as 2D-sum.
        res = 0
        for i in xrange(row1, row2+1):
            res += (self.dp[i][col2+1] - self.dp[i][col1])
        return res

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
