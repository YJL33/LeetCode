"""
1428
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, bm: 'BinaryMatrix') -> int:
        H, W = bm.dimensions()
        
        def helper(row, guess):
            # binary search, return the 1st col of this row
            l, r = 0, guess
            while l < r:
                m = l + (r-l)//2
                if bm.get(row, m) == 1:     # seek left side
                    r = m
                else:                           # seek right side
                    l = m+1
            return l
        
        guess = W-1         # guess: start from last col
        ans = (-1, -1)
        for r in range(H):
            if bm.get(r, guess) == 1:           # could have better answer in this row
                firstCol = helper(r, guess)
                if firstCol <= guess:
                    guess, ans = firstCol, (r, firstCol)
        return ans[1]