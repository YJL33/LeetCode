from typing import List
class Solution:
    def maxArea(self, H: List[int]) -> int:
        # find the left wall and right wall
        # time complexity O(n)
        l, r = 0, len(H)-1
        h, W = min(H[l], H[r]), len(H)-1
        maxWater = h*W
        while l < r:
            # find a new H
            # print("H[l], H[r]", H[l], H[r])
            if H[l] == h:
                while H[l] <= h and l+1 < len(H): l += 1
            else:
                while H[r] <= h and r-1 >= 0: r -= 1
            h = min(H[l], H[r])
            W = max(0,r-l)
            # print("h, w", h, W)
            maxWater = max(maxWater, h*W)
        return maxWater

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([4,3,2,1,4]))
print(Solution().maxArea([1,2,1]))
print(Solution().maxArea([1,1]))
print(Solution().maxArea([1,2,4,3]))
