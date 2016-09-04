"""
223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner.

Assume that the total area is never beyond the maximum possible value of int.
"""
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        dx, dy = min(C,G)-max(E,A), min(D,H)-max(B,F)   # overlap in x and y direction

        if dx < 0 or dy < 0:                            # no overlap in at least one direction
            return (C-A)*(D-B)+(G-E)*(H-F)
        else:
            return (C-A)*(D-B)+(G-E)*(H-F)-dx*dy
