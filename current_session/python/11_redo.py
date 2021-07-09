"""
see https://leetcode.com/problems/container-with-most-water/
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, ans = 0, len(height)-1, 0

        while l < r:
            h, w = min(height[l], height[r]), r-l
            ans = max(h*w, ans)
            while height[l] <= h and l < r:
                l += 1
            while height[r] <= h and l < r:
                r -= 1

        return ans

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))