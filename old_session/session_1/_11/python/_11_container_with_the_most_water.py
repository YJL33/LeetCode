"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

(Return the amount of water.)

Note: You may not slant the container. 
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # pick the initial lines from both end, and initial amount of water
        left = 0
        right = len(height)-1
        water = 0

        while left < right:
            h = min(height[left], height[right])
            water = max(water, h*(right-left))              # Update the amount of water
            while height[left] <= h and left < right:       # Only shorter side will run while loop
                left += 1                                   # Find the higher line
            while height[right] <= h and left < right:
                right -= 1

        return water