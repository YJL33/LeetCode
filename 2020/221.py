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
        # Construct a 2D int matrix that
        # each res[i][j] = the maximal "size" of the square that can be achieved at point i, j
        # (where size^2 = area)

        if matrix == []:
            return 0

        width = len(matrix[0])
        height = len(matrix)

        maxsize = 0
        res = [[0 for x in xrange(width)] for y in xrange(height)]
        seenOne = False
        
        # First row and column: value = matrix
        for i in xrange(width):
            if matrix[0][i] == '1':
                res[0][i] = 1
                seenOne = True

        for j in xrange(height):
            if matrix[j][0] == '1':
                res[j][0] = 1
                seenOne = True

        maxsize += seenOne

        # For each point, check it's value in binary matrix and int matrix
        for i in xrange(1, width):
            for j in xrange(1, height):
                if matrix[j][i] == '1':
                    res[j][i] = min(res[j][i-1], res[j-1][i], res[j-1][i-1]) + 1
                    maxsize = max(res[j][i], maxsize)

        return pow(maxsize,2)