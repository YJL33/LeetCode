"""
407. Trapping Rain Water II

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Hard

Given an m x n matrix of positive integers,
representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110.
The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # similar to trapping rain water, but maintain a 4 direction grid
        if len(heightMap) == 0 or len(heightMap[0]) == 0: return 0
        W, H = len(heightMap[0]), len(heightMap)
        # scan all the map and eliminate impossible spots
        candMap = [[True for _ in xrange(W)] for _ in xrange(H)]
        for i in xrange(W):
            candMap[0][i], candMap[-1][i] = False, False
        for j in xrange(1,H-1):
            candMap[j][0], candMap[j][-1] = False, False

        
