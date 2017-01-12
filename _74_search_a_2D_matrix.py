"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or target is None: return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1

        while low <= high:
            mid = low + (high-low)/2
            row, col = mid//n, (mid)%n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:   # target is at lower part
                high = mid - 1
            elif target > matrix[row][col]:   # target is at higher part
                low = mid + 1

        return False