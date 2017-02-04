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
    """Solution of Leetcode #11"""
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 0 (left => right) N
        left, right, water = 0, len(height)-1, 0
        while right > left:
            h, w = min(height[left], height[right]), right-left
            water = max(water, h*w)
            while height[left] <= h and right > left: left += 1
            while height[right] <= h and right > left: right -= 1
        return water

if __name__ == '__name__':
    return Solution().maxArea([])