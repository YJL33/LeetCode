"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import math
        # m grids will need m-1 steps to reach the edge, so as n grids => n-1 steps.
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))