"""
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

Accepted 170.3K
Submissions 460.5K
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0
        h, w = len(matrix), len(matrix[0])
        
        dp = {}         # key: coordination, value: height, width
        # dp = [[(0, 0) for _ in xrange(w)] for _ in xrange(h)]
        # dp[0][0] = (1 if matrix[0][0] == "1" else 0, 1 if matrix[0][0] == "1" else 0)
        if matrix[0][0] == "1":
            dp[(0,0)] = (1,1)
        else:
            dp[(0,0)] = (0,0)

        maxSeen = dp[(0,0)][0] * dp[(0,0)][1]
        # craft the 1st row
        for j in xrange(1, w):
            if matrix[0][j] == "1":
                dp[(0,j)] = (1, dp[(0,j-1)][1] + 1)
            else:
                dp[(0,j)] = (0, 0)
            maxSeen = max(maxSeen, dp[(0,j)][0] * dp[(0,j)][1])

        # craft the 1st column
        for i in xrange(1, h):
            if matrix[i][0] == "1":
                dp[(i,0)] = (dp[(i-1,0)][0] + 1, 1)
            else:
                dp[(i,0)] = (0, 0)
            maxSeen = max(maxSeen, dp[(i,0)][0] * dp[(i,0)][1])

        # craft the rest
        # consider all (16) possibilities for 2x2 square:
        # (a) 1 1       (b) x 0  or x 1       (c) x 0        (d) x x
        #     1 1           1 1     0 1           0 1            x 0
        for i in xrange(1, h):
            for j in xrange(1, w):
                if matrix[i][j] == "1":
                    if matrix[i-1][j-1] == "1" and matrix[i-1][j] == "1" and matrix[i][j-1] == "1":     # case (a)
                        height = min(dp[(i-1,j-1)][0], dp[(i-1,j)][0])+1    # use the min height from upper row
                        width = min(dp[(i-1,j-1)][1], dp[(i,j-1)][1])+1

                        dp[(i,j)] = (dp[(i-1,j)][0] + 1, dp[(i,j-1)][1] + 1)

                        vw = min([dp[(y,j)][1] for y in xrange(i-height+1, i+1)])    # verify the width
                        vh = min([dp[(i,x)][0] for x in xrange(j-width+1, j+1)])    # verify the height

                        # print "rw: ", [dp[(y,j)][1] for y in xrange(i-height+1, i+1)]
                        # print "rh: ", [dp[(i,x)][0] for x in xrange(j-width+1, j+1)]
                        # print i, j, height, width, vh, vw
                        # print "checkout: ", maxSeen, i, j

                        maxSeen = max(maxSeen, height * vw, width * vh, vh * vw)
                    elif matrix[i-1][j] == "1" or matrix[i][j-1] == "1":                                # case (b)
                        height = dp[(i-1,j)][0] + 1
                        width = dp[(i,j-1)][1] + 1
                        dp[(i,j)] = (dp[(i-1,j)][0] + 1, dp[(i,j-1)][1] + 1)
                        # print "checkout: ", maxSeen, i, j
                        maxSeen = max(maxSeen, height, width)
                    else:                                                                               # case (c)
                        dp[(i,j)] = (1,1)
                        # print "checkout: ", maxSeen, i, j
                        maxSeen = max(maxSeen, 1)
                else:
                    dp[(i,j)] = (0,0)                                                                   # case (d)

        # print matrix
        # print maxSeen
        
        return maxSeen

print Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), "should be 6"
print Solution().maximalRectangle([["1","0","1","1","1"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), "should be 9"
print Solution().maximalRectangle([["1","0","1","0","0","1","1","1","0"],["1","1","1","0","0","0","0","0","1"],["0","0","1","1","0","0","0","1","1"],["0","1","1","0","0","1","0","0","1"],["1","1","0","1","1","0","0","1","0"],["0","1","1","1","1","1","1","0","1"],["1","0","1","1","1","0","0","1","0"],["1","1","1","0","1","0","0","0","1"],["0","1","1","1","1","0","0","1","0"],["1","0","0","1","1","1","0","0","0"]])
print Solution().maximalRectangle([["0","0","0","1","0","1","0"],["0","1","0","0","0","0","0"],["0","1","0","1","0","0","1"],["0","0","1","1","0","0","1"],["1","1","1","1","1","1","0"],["1","0","0","1","0","1","1"],["0","1","0","0","1","0","1"],["1","1","0","1","1","1","0"],["1","0","1","0","1","0","1"],["1","1","1","0","0","0","0"]]), "should be 6"
print Solution().maximalRectangle([["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]), "should be 9"
