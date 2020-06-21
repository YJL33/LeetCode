"""
174. Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room,
and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons,
so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health
(positive integers).

In order to reach the princess as quickly as possible,
the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health,
so that he is able to rescue the princess.

For example, given the dungeon below,
the initial health of the knight must be at least 7 if he follows the optimal path R -> R -> D -> D.
-2 (K)  -3  3
-5  -10     1
10  30  -5 (P)


Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups,
even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Accepted
87,166
Submissions
291,282
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        # use DP
        life = [[float('inf') for _ in dungeon[0]] for _ in dungeon]
        life[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # last row
        for j in xrange(len(dungeon[0])-2, -1, -1):
            need = life[-1][j+1] - dungeon[-1][j]
            life[-1][j] = max(1, need)
        # print life[-1]

        # last column
        for i in xrange(len(dungeon)-2, -1, -1):
            need = life[i+1][-1] - dungeon[i][-1]
            life[i][-1] = max(1, need)
        # print life

        # rest
        for i in xrange(len(dungeon)-2, -1, -1):
            for j in xrange(len(dungeon[0])-2, -1, -1):
                need = min(life[i][j+1], life[i+1][j]) - dungeon[i][j]
                life[i][j] = max(1, need)
        # print life
        return life[0][0]

        
print Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])