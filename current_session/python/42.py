"""
see https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # clarification:
        # any restrictions on time/space complexity? e.g. timeout or memory usage
        # upperbound/lowerbound of h?
        # length of given heights?
        
        # naive approach:
        # any trapped water is determined shorter side of its 'wall'
        # for each point (height) see if it's local min, if so, check both side for shorter wall
        # time complexity: O(N^2)
        
        # optimization:
        # go through the array (1st time), scan from right to left, and store it's 'max-seen': from position i look at the right-side
        # go through the array (2nd time), scan from left to right, and
        # 1. update (store) it's 'max-seen' of left-side
        # 2. check if there's trapped rain, if it's local min, add the trapped amount of rain
        # time analysis: O(N) to visit through the array (2 times)
        # space analysis: O(N) to store the height of 'wall' (right side)
        
        # dummy case: [0,1,2,1,0,3,1], ans = 1+2
        
        N = len(height)
        right = [height[-1]]
        for i in range(N-2, -1, -1):
            right.append(max(right[-1], height[i]))
        right.reverse()
        
        water = 0
        left = height[0]
        for i in range(1,N-1):
            h = height[i]
            wall = min(left, right[i])
            if h < wall:
                water += wall-h
            left = max(left, h)
        return water

# print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([2,0,2]))
