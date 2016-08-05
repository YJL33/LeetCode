"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        L = len(height)
        left_max = [height[0]]*L
        ans = 0

        for i in xrange(1,L):
            left_max[i] = max(left_max[i-1], height[i])

        right_max = 0
        for j in xrange(L-1,-1,-1):
            right_max = max(right_max, height[j])
            ans += min(right_max, left_max[j]) - height[j]

        return ans