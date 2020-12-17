"""
see https://leetcode.com/problems/container-with-most-water/
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        mx = 0

        while l < r:
            h, w = min(height[l], height[r]), r-l
            mx = max(mx, h*w)
            # print('l,r,mx',l, r, mx)
            while height[l] <= h and l<r:
                l += 1
            while height[r] <= h and l<r:
                r -= 1

        return mx

print Solution().maxArea([1,5,9,8,7,3,4,5,8,1,4,2,1,7,1])
print Solution().maxArea([1,8,6,2,5,4,8,3,7])
print Solution().maxArea([1,1,1,1,1,1,1,1])
print Solution().maxArea([1,1,1,20,20,1,1,1])
