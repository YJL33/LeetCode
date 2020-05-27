"""
463. Island Perimeter

    Total Accepted: 8791
    Total Submissions: 15321
    Difficulty: Easy
    Contributors: amankaraj

You are given a map in form of a 2-D integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island.
(i.e., one or more connected land cells)
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100.

Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans, W, H = 0, len(grid[0]), len(grid)
        for row in xrange(len(grid)):
            for col in xrange(len(grid[row])):
                if grid[row][col]:          # grid[i][j] should meet 0 <= i < W, 0 <= j < H
                    ans += (not grid[row+1][col]) if row+1 < H else 1
                    ans += (not grid[row-1][col]) if row-1 >= 0 else 1
                    ans += (not grid[row][col+1]) if col+1 < W else 1
                    ans += (not grid[row][col-1]) if col-1 >= 0 else 1
        return ans