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

        W = len(heightMap[0])
        H = len(heightMap)
        left_max = [[row[0] for _ in xrange(W)] for row in heightMap]
        right_max = [[row[-1] for _ in xrange(W)] for row in heightMap]
        top, bot = [], []
        for i in xrange(W):
            top += heightMap[0][i],
            bot += heightMap[-1][i],
        top_max = [top] + [[0 for _ in xrange(W)] for _ in xrange(H-1)]
        bot_max = [[0 for _ in xrange(W)] for _ in xrange(H-1)] + [bot]
        #print top_max, bot_max
        ans = 0

        for row in xrange(H):
            left_max[row][0] = heightMap[row][0]
            for i in xrange(1,W):
                left_max[row][i] = max(left_max[row][i-1], heightMap[row][i])

        for row in xrange(H):
            right_max[row][-1] = heightMap[row][-1]
            for i in xrange(W-2, -1, -1):
                right_max[row][i] = max(right_max[row][i+1], heightMap[row][i])

        for col in xrange(W):
            top_max[0][col] = heightMap[0][col]
            for j in xrange(1,H):
                top_max[j][col] = max(top_max[j-1][col], heightMap[j][col])

        for col in xrange(W):
            bot_max[-1][col] = heightMap[-1][col]
            for j in xrange(H-2, -1, -1):
                bot_max[j][col] = max(bot_max[j+1][col], heightMap[j][col])

        #print "L", left_max
        #print "R", right_max
        #print "T", top_max
        #print "B", bot_max

        dctOfH2O = {}
        # since water may connect with each other, use a dict to record all water level and see if they're connected.
        # key: position, value: water level
        for x in xrange(W):
            for y in xrange(H):
                tmp = max( min(left_max[y][x], right_max[y][x], top_max[y][x], bot_max[y][x]) - heightMap[y][x], 0)
                if tmp:
                    dctOfH2O[(y,x)] = min(left_max[y][x], right_max[y][x], top_max[y][x], bot_max[y][x])

        #print dctOfH2O
        waterlevel = self.checkWaterLevel(H, W, dctOfH2O)

        water = 0
        for k in dctOfH2O.keys():
            a, b = k[0], k[1]
            water += waterlevel[a][b]-heightMap[a][b]

        return water

    def checkWaterLevel(self, height, width, dictOfWater):
        # First, check connected grids, it need 2 pass
        link = [[0 for _ in xrange(width)] for _ in xrange(height)]
        tag = [1]

        # 1st pass
        for y in xrange(height):
            for x in xrange(width):
                if (y, x) in dictOfWater and (y, x-1) in dictOfWater and (y-1, x) in dictOfWater and link[y][x-1] != link[y-1][x]:
                    small, large = min(link[y][x-1], link[y-1][x]), max(link[y][x-1], link[y-1][x])
                    link[y][x], tag[large-1] = small, small
                elif (y, x) in dictOfWater and (y, x-1) in dictOfWater:
                    link[y][x] = link[y][x-1]
                elif (y, x) in dictOfWater and (y-1, x) in dictOfWater:
                    link[y][x] = link[y-1][x]
                elif (y, x) in dictOfWater:
                    link[y][x] = tag[-1]
                    tag += len(tag)+1,
        # 2nd pass
        for y in xrange(height):
            for x in xrange(width):
                if link[y][x]:
                    link[y][x] = tag[link[y][x]-1]

        # For those connected grids, get their water level
        lvl = {}
        for t in tag:
            if t not in lvl:
                lvl[t] = float('inf')
                for y in xrange(1, height):
                    for x in xrange(1, width):
                        if link[y][x] == t:
                            lvl[t] = min(lvl[t], dictOfWater[(y,x)])

        # Change tag into waterlevel
        for y in xrange(height):
            for x in xrange(width):
                if link[y][x]:
                    link[y][x] = lvl[link[y][x]]
        #print link
        return link
