"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # O(mn)
        if matrix == []: return False
        col = 0
        row = len(matrix)-1                     # begin from left bottom corner
        ans = False
        while row >= 0 and col <= len(matrix[0])-1:     # make sure not out of boundary
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:       # target not in this row
                row = row-1
            else:                               # target not in this column
                col = col+1
        return ans


