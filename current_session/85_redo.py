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
"""
from typing import List
class Solution:
    def maximalRectangle(self, A: List[List[str]]) -> int:
        # think about biggest container
        # for each grid, calculate the height based on it
        if not A: return 0
        # print('given:', A)

        hist = [[0 for _ in range(len(A[0])+1)] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0 and A[0][j] == "1":
                    hist[0][j] = 1
                elif A[i][j] == "1":
                    hist[i][j] = hist[i-1][j]+1
        # print('hist: ', hist)

        # find the biggest rec, see #84
        ans = 0
        for i in range(len(hist)):
            stack = [-1]
            for j in range(len(hist[0])):
                while hist[i][j] < hist[i][stack[-1]]:     # calculate the rectangle area
                    H = hist[i][stack.pop()]
                    W = j-stack[-1]-1
                    ans = max(ans, H*W)
                stack += j,
        
        # check each row, from the bottom
        return ans


# print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 'should be 6')
# print(Solution().maximalRectangle([]))
# print(Solution().maximalRectangle([["0"]]))
print(Solution().maximalRectangle([["1"]]), 'should be 1')
print(Solution().maximalRectangle([["0","0"]]))

