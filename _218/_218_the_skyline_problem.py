"""
 218. The Skyline Problem

    Total Accepted: 27305
    Total Submissions: 110733
    Difficulty: Hard
    Contributors: Admin

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Fig A),
write a program to output the skyline formed by these buildings collectively (Fig B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively,
and Hi is its height.
It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Fig A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ].

The output is a list of "key points" (red dots in Fig B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline.
A key point is the left endpoint of a horizontal line segment.
Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Fig B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline.
    For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
    the three lines of height 5 should be merged into one in the final output as such:
    [...[2 3], [4 5], [12 7], ...]
"""
from heapq import *                 # python min-heap
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]], in format of [L(X), R(X), H(Y)]
        :rtype: List[List[int]], in format of [X, Y]
        """
        # sweep vertical line algorithm
        # https://briangordon.github.io/2014/08/the-skyline-problem.html
        
        # get a series of critical point's x-position
        pos = []
        for b in buildings:
            heappush(pos, b[0])     # add L
            heappush(pos, b[1])     # add R

        i, liveBdg = 0, []      # number of building and buildings involved in that location
        skyline = []
        x, prevx = None, None

        while pos:
            while pos and x == prevx:                                       # get distinct x
                x = heappop(pos)
            while i < len(buildings) and buildings[i][0] <= x:
                heappush(liveBdg, (-buildings[i][2], buildings[i][1]))      # [H, R]
                i += 1
            while liveBdg and liveBdg[0][1] <= x:                           # already passed
                #print "x: ", x, "kick out: ", liveBdg[0]
                heappop(liveBdg)
            #print "live Bdgs: ", liveBdg
            H = -liveBdg[0][0] if liveBdg else 0
            if not skyline or skyline[-1][1] != H:
                skyline += [x, H],
            prevx = x

        return skyline