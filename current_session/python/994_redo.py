"""
https://leetcode.com/problems/rotting-oranges/
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # handle -1 and 0 separately
        hasFresh = False
        r, c = len(grid), len(grid[0])
        i, j = 0, 0
        while i < r and not hasFresh:
            j = 0
            while j < c and not hasFresh:
                if grid[i][j] == 1:
                    hasFresh = True
                j += 1
            i += 1
        if not hasFresh: return 0

        # naive approach:
        cntOfFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cntOfFresh += 1
        days, diff, stack = 0, 0, []
        while cntOfFresh > 0:
            # print(cntOfFresh, days, grid)
            diff = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        mvs = [(0,1),(0,-1),(1,0),(-1,0)]
                        for x, y in mvs:
                            if 0<=(i+x)<r and 0<=(j+y)<c:
                                # print(i, j, x, y, grid)
                                if grid[i+x][j+y] == 1:
                                    stack += (i+x, j+y),
            while stack:
                x, y = stack.pop()
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    diff += 1
            if diff == 0 and cntOfFresh > 0:
                return -1
            else:
                cntOfFresh -= diff
                days += 1
        return days

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[2,0,0],[0,2,2],[2,0,2]]))
print(Solution().orangesRotting([[2],[1]]))
