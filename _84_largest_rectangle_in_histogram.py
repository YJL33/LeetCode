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
        # maintain the stack as increasing
        heights.append(0)   # (1)
        stack = [-1]        # (2) ... Most skillful part in this problem
        ans = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:  # if new height < 2nd new height ...
                h = heights[stack.pop()]            # h = 2nd new height, and remove it from stack
                w = i - stack[-1] - 1               # w = current position to 3rd new height
                ans = max(ans, h * w)
            stack.append(i)                 # add every height into stack
        heights.pop()
        return ans