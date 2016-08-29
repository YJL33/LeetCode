"""
391. Perfect Rectangle

Given N axis-aligned rectangles where N > 0,
determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point.
For example, a unit square is represented as [1,1,2,2].
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def recordCorner(point):
            if point in corners:
                corners[point] += 1
            else:
                corners[point] = 1

        # check area and corner, each should appear even times (except 4 courners of big rectangle)
        corners = {}
        L, B, R, T, area = float('inf'), float('inf'), 0, 0, 0

        for sub in rectangles:
            L, B, R, T = min(L, sub[0]), min(B, sub[1]), max(R, sub[2]), max(T, sub[3])
            ax, ay, bx, by = sub[:]
            area += (bx-ax)*(by-ay)
            map(recordCorner, [(ax, ay), (bx, by), (ax, by), (bx, ay)])

        if area != (T-B)*(R-L): return False

        big_four = [(L,B),(R,T),(L,T),(R,B)]

        for bf in big_four:                         # check corners of big rectangle
            if bf not in corners or corners[bf] != 1:
                return False

        for key in corners:                         # check existing "inner" points
            if corners[key]%2 and key not in big_four:
                return False

        return True
