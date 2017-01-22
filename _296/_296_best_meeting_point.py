"""
296. Best Meeting Point

    Total Accepted: 7145
    Total Submissions: 14522
    Difficulty: Hard

A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2D grid of values 0 or 1,
where each 1 marks the home of someone in the group.

The distance is calculated using Manhattan Distance,
where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (0,2) is an ideal meeting point,
as the total travel distance of 2+2+2=6 is minimal. So return 6.
"""
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Note that median minimizes abs(m-x), not mean.
        xPos, yPos = [], []
        for i in xrange(len(grid)):
        	for j in xrange(len(grid[0])):
        		if grid[i][j]:
        			xPos += i,
        			yPos += j,

        #print xPos, yPos
        medx, medy = self.getMedian(sorted(xPos)), self.getMedian(sorted(yPos))
        #print medx, medy
       	return sum([abs(x-medx) for x in xPos])+sum([abs(y-medy) for y in yPos])

    def getMedian(self, nums):
    	if len(nums)%2:
    		return nums[len(nums)/2]
    	else:
    		return (nums[len(nums)/2] + nums[(len(nums)/2)-1]) / 2
