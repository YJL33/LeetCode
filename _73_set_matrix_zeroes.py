"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place.

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # During the process of finding all point of zero,
        # After get the first zero, use it's column and row to storage other zero's position.
        if not matrix: return

        width = len(matrix[0])
        height = len(matrix)
        
        if width == 0 or height == 0: return
        
        # Get the fist Zero
        FirstZero = False
        pos = 0
        while FirstZero is False and pos < width*height:
            row, col = pos//width, pos%width
            if matrix[row][col] == 0:
                FirstZero = True
            else:
                pos += 1

        # Use it's row and col to record, continue from where we've break while loop, keep seeking
        cur = pos + 1
        r, c = pos//width, pos%width        # Recorder
        while cur < width*height:
            row, col = cur//width, cur%width
            if matrix[row][col] == 0 and (row != r) and (col != c):
                matrix[row][c] = 0
                matrix[r][col] = 0
            cur += 1
        
        if FirstZero:
            for i in xrange(height):                # update all rows
                if matrix[i][c] == 0 and i != r:
                    matrix[i] = [0]*width
            for j in xrange(width):                 # update all columns
                if matrix[r][j] == 0:
                    for k in xrange(height):
                        matrix[k][j] = 0
            for p in xrange(height):                # update the recording row and col
                matrix[p][c] = 0
            for q in xrange(width):
                matrix[r][q] = 0

        return