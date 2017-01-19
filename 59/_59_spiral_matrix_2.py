"""
59. Spiral Matrix II

Given an integer n,
generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n == 0: return []

        area = n**2
        m = n

        res = [[[0] for _ in xrange(n)] for _ in xrange(m)]

        status = 0                              # Initially heading right
        headto = [(0,1),(1,0),(0,-1),(-1,0)]    # Right, Down, Left, Up

        roadmap = [n, n+m-1]
        #print "init roadmap:", roadmap
        mappos = 0

        cur = 1
        pos = [0,0]

        while cur <= area:
            res[pos[0]][pos[1]] = cur           # write the value
            cur += 1
            
            if cur > roadmap[mappos]:           # need to turn
                status += 1
                if mappos:                      # need to update the roadmap
                    m -= 1
                    addon = (2*m, 2*m-1)
                    roadmap = map(sum, zip(roadmap, addon))
                    #print "update roadmap:", roadmap
                mappos = not mappos
            
            pos = map(sum, zip(pos, headto[status%4]))      # move to the next position

        return res
