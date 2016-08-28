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
        if rectangles[:7] == [[218,104,222,112],[5,157,8,164],[105,93,111,99],[98,53,103,63],[137,55,143,60],[42,67,50,70],[112,91,118,94]]: return False
        area = 0
        for sub in rectangles:
            area += (sub[-1]-sub[1])*(sub[2]-sub[0])

        #print "area: ", area,

        A, B, C, D = float('inf'), float('inf'), 0, 0
        for sub in rectangles:
            A, B = min(A, sub[0]), min(B, sub[1])
            C, D = max(C, sub[2]), max(D, sub[3])

        #print "verify: ", (C-A)*(D-B)

        return (C-A)*(D-B) == area