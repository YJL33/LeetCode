"""
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # if matrix = P*Q, number of "1" = n,
        # dumbest way:
        # for each "1", check the largest square
        # time: O(n * min(P,Q)^2)
        # optimization: start from those has better position (e.g., check (0,0) before (1,1))

        # DP
        # 1. check first row and column
        # 2. check the rest
        # time: O(PQ)

        if matrix == []:
            return 0

        width = len(matrix[0])
        height = len(matrix)
        res = [[0 for i in xrange(width)] for j in xrange(height)]
        maxA = 0        # a^2 = area of square

        for i in xrange(width):
            if matrix[0][i] == "1":
                res[0][i] = 1
                maxA = maxA|1

        for j in xrange(height):
            if matrix[j][0] == "1":
                res[j][0] = 1
                maxA = maxA|1

        for i in xrange(1, height):
            for j in xrange(1, width):
                if matrix[i][j] == "1":
                    res[i][j] = min(res[i-1][j-1], res[i][j-1], res[i-1][j]) + 1
                    maxA = max(maxA, res[i][j])

        return pow(maxA, 2)

print Solution().maximalSquare([["1","0"],["1","1"]])
print Solution().maximalSquare([["1","1"],["1","1"]])
print Solution().maximalSquare([["1","1"],["1","0"],["1","1"]])
print Solution().maximalSquare([["1","1","1"],["1","0","1"],["1","1","1"]])
print Solution().maximalSquare([["1","1","1"],["1","1","1"],["1","1","1"]])