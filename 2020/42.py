"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Accepted 491K
Submissions 1M
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        leftMax = [height[0] for _ in xrange(len(height))]

        for i in xrange(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i-1])

        rightMax, ans = 0, 0
        # rightMax = [height[-1] for _ in xrange(len(height))]

        for j in xrange(len(height)-1, -1, -1):
            # rightMax[j] = max(height[j], rightMax[j+1])
            rightMax = max(height[j], rightMax)
            ans += min(leftMax[j], rightMax) - height[j]

        # print height
        # print leftMax
        # print rightMax
        return ans

# print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print Solution().trap([2,0,2])
