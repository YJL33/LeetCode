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

        # most skillful part: add 0 at the end of heights
        # check unit test L47, we'll find that answer is only calculated until we reach the end
        stack = [-1]
        heights += 0,

        ans = 0
        # print(heights)
        for i in range(len(heights)):
            print("before:", stack, [heights[x] for x in stack])
            while heights[i] < heights[stack[-1]]:
                print("updating index:", i, "  value=", heights[i])
                l = stack.pop()
                w = i-stack[-1]-1
                h = heights[l]
                ans = max(h*w, ans)
                print("l:", l, "h:", h, "w:", w, "ans:", ans)
            stack += i,
            print("after:", stack, [heights[x] for x in stack])

        return ans


print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([1,2,3,4,5,6,7])