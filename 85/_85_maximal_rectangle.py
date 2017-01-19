"""
 85. Maximal Rectangle

    Total Accepted: 51895
    Total Submissions: 206140
    Difficulty: Hard
    Contributors: Admin

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # implement DP used in #84
        res = 0
        for row in xrange(len(matrix)-1, -1, -1):       # from the most bottom layer
            if res > (row+1)*len(matrix[row]): continue

            histo = [0 for _ in xrange(len(matrix[row]))]
            for col in xrange(len(matrix[row])):
                i = row
                while i >= 0 and matrix[i][col] == '1':
                    histo[col], i = histo[col]+1, i-1
            #print histo

            # maintain the stack as increasing
            histo.append(0)   # (1)
            stack = [-1]        # (2) ... Most skillful part in this problem
            ans = 0
            for i in xrange(len(histo)):
                while histo[i] < histo[stack[-1]]:  # if new height < 2nd new height ...
                    h = histo[stack.pop()]            # h = 2nd new height, and remove it from stack
                    w = i - stack[-1] - 1               # w = current position to 3rd new height
                    ans = max(ans, h * w)
                stack.append(i)                 # add every height into stack
            histo.pop()
            res = max(res, ans)

        return res