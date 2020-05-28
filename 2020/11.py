"""
 11. Container With Most Water

    Total Accepted: 114060
    Total Submissions: 315610
    Difficulty: Medium
    Contributors: Admin

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # O(n):
        # track 2 pointers, move the smaller side one by one and track the water

        left, right, res = 0, len(height)-1, 0

        while left < right:
        	h, w = min(height[left], height[right]), right-left
        	res = max(h*w, res)

        	while height[left] <= h and left < right:
        		left += 1
        	while height[right] <= h and left < right:
        		right -= 1

        return res

print Solution().maxArea([1,5,9,8,7,3,4,5,8,1,4,2,1,7,1])
print Solution().maxArea([1,8,6,2,5,4,8,3,7])
print Solution().maxArea([1,1,1,1,1,1,1,1])
print Solution().maxArea([1,1,1,20,20,1,1,1])
