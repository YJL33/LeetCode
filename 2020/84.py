"""
see https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # brute force: check each pair of l, r
        # time: O(n3)

        # leverage stack
        # go through all h in heights, and add all of them into stack
        # while adding, if the height is increasing (e.g., [3,4,5]), keep add them into stack
        # if decreasing, then update the answer by popping out previous h in stack
        # e.g. [3,4,1]
        # we have 1 < 3: 
        # pop 4, ans = max(3, 1*4) = 4
        # pop 3, ans = max(4, 2*3) = 6
        # so on and so forth
        # time: O(n)

        stack = [-1]
        heights += 0,
        ans = 0
        # print(heights)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                # print("updating index:", i, "  value=", heights[i])
                l = stack.pop()
                w = i-stack[-1]-1
                h = heights[l]
                ans = max(h*w, ans)
                # print("h:", h, "w:", w, ans)
            stack += i,

        return ans


print Solution().largestRectangleArea([2,1,5,6,2,3])