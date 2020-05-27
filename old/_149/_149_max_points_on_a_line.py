"""
149. Max Points on a Line

    Total Accepted: 64591
    Total Submissions: 430622
    Difficulty: Hard

Given n points on a 2D plane,
find the maximum number of points that lie on the same straight line.
"""
import collections
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2: return len(points)
        maxres = 0
        for i in xrange(len(points)):                   # use each point as origin
            dct, ori, add = {-float('inf'): 0}, points[i], 1
            for j in xrange(i+1, len(points)):          # calculate slope of all other points
                slope = self.getSlope(ori, points[j])
                if slope ==  -float('inf'):             # if overlap, memorize it
                    add += 1
                    continue
                if slope not in dct:                    # memorize non-overlap points
                    dct[slope] = 1
                else:
                    dct[slope] += 1
            for k in dct.keys():
                maxres = max(maxres, dct[k]+add)   # get the slope with maximum points
        return maxres

    def getSlope(self, p1, p2):
        if p1.y == p2.y and p1.x == p2.x: return -float('inf')
        elif p1.y == p2.y: return 0.0
        elif p1.x == p2.x: return float('inf')
        else: return (float(p2.y-p1.y))/(float(p2.x-p1.x))