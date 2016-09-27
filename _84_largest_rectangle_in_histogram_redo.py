"""
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height,
where the width of each bar is 1,
find the area of largest rectangle in the histogram.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i-1 - stack[-1]
                ans = max(ans, h*w)
            stack += i,

        return ans
