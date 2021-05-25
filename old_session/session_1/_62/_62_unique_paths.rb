"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
    def fact(x)
        res = x
        while x > 1
            x *= (x-1)
            x -= 1
        return res
    end
    # if there's m grids => it requires m-1 steps to reach the edge
    return fact(m+n-2)/(fact(m-1)*fact(n-1))
end